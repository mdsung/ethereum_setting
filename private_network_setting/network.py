import os
import time 
import json
from web3 import Web3, HTTPProvider

from method import run_command, write_file

class Network:
    def __init__(self, node_dir, max_peer, network_id, monitoring, influx_db, rpc, node):
        self.node_dir = node_dir
        self.dir_name_list = os.listdir(node_dir)
        self.max_peer = max_peer
        self.network_id = network_id
        
        self.monitoring_ip = monitoring["ip"]
        self.monitoring_port = monitoring["port"]
        self.monitoring_id = monitoring["id"]
        
        self.influx_db_ip = influx_db["ip"]
        self.influx_db_port = influx_db["port"]
        self.influx_db_name = influx_db["db_name"]
        
        self.rpc_ip = rpc["ip"]
        self.rpc_port = lambda i: rpc["port"] + i
        
        self.node_port = lambda i: node["port"] + i

        self.enode_url_list = []

    def run_geth(self, i, dir):
        command = f"geth \
                    --nat none \
                    --nousb \
                    --syncmode full \
                    --ipcdisable \
                    --maxpeers {self.max_peer} \
                    --networkid {self.network_id} \
                    --metrics.influxdb \
                    --metrics.influxdb.endpoint http://{self.influx_db_ip}:{self.influx_db_port} \
                    --metrics.influxdb.database \"{self.influx_db_name}{i}\" \
                    --port {self.node_port(i)} \
                    --ethstats {dir}:{self.monitoring_id}@{self.monitoring_ip}:{self.monitoring_port} \
                    --allow-insecure-unlock \
                    --datadir ./nodes/{dir} \
                    --http \
                    --http.addr \"0.0.0.0\" \
                    --http.port {self.rpc_port(i)} \
                    --http.corsdomain \"*\" \
                    --http.api \"admin, eth, debug, miner, net, txpool, personal, web3\" \
                    --nodiscover \
                    --metrics \
                    --verbosity 6 \
                    2>> {self.node_dir}/{dir}/geth.log &"
        run_command(command)    
        
    def parse_enode_url(self, i):
        self.w3 = Web3(HTTPProvider(f"http://{self.rpc_ip}:{self.rpc_port(i)}"))
        enode_url = ""
        while True:
            if self.w3.isConnected():
                enode_url = self.w3.geth.admin.node_info()["enode"]        
                break
        
        self.enode_url_list.append(enode_url)

    def add_static_json(self, i):
        file_name = f"{self.node_dir}/{self.dir_name_list[i]}/static-nodes.json"
        write_file(file_name, json.dumps(self.enode_url_list))

    def create_network(self):
        for i, dir in enumerate(self.dir_name_list):
            self.run_geth(i, dir)
            self.parse_enode_url(i)
            if i != len(self.dir_name_list) - 1:
                self.add_static_json(i + 1)
        


    

        