import os

from web3 import Web3, HTTPProvider

from method import run_command, validate_dir, create_dir
from reset import Reset
from env import Env
from account import Account
from genesis import Genesis
from network import Network

NUM_OF_NODE = 2

NODE_DIR = "./nodes"
NETWORK_DIR = "./Network"

GENESIS_TEMPLATE_FILE = f"{NETWORK_DIR}/Genesis_template.json" 
GENESIS_FILE = f"{NETWORK_DIR}/Genesis.json" 

NETWORK_PARAMS={
    "node_dir" : NODE_DIR,
    "max_peer" : 50,
    "network_id" : 1234,
    "monitoring" : {"ip":"127.0.0.1", "port":"3000", "id":"hello"},
    "influx_db" : {"ip":"10.19.12.59", "port":"8086", "db_name":"test"},
    "rpc" : {"ip":"127.0.0.1", "port":10000},
    "node" : {"port":30000},
}

def main():
    create_dir(NETWORK_DIR)

    # delete old data
    reset = Reset(NODE_DIR)
    reset.reset()

    # Create new data folder
    env = Env(NUM_OF_NODE, NODE_DIR)
    env.create()

    # Create Account
    account = Account(NODE_DIR)
    account.create()

    # Init Geth(Genesis)
    genesis = Genesis(GENESIS_TEMPLATE_FILE, GENESIS_FILE)
    genesis.create_genesis_json(account.public_key_list)
    genesis.init_geth(NODE_DIR)

    # Create_network
    network = Network(**NETWORK_PARAMS)
    network.create_network()


    # Validate network
    rpc_ip = NETWORK_PARAMS["rpc"]["ip"]
    w3 = Web3(HTTPProvider(f"http://{rpc_ip}:10000"))
    print(w3.net.peerCount)

if __name__ =="__main__":
    main()