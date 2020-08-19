import os

from web3 import Web3, HTTPProvider

from method import run_command, validate_dir, create_dir
from reset import Reset
from env import Env
from account import Account
from genesis import Genesis
from network import Network

NUM_OF_NODE = int(os.environ["NODES"])

NODE_DIR = "./nodes"
NETWORK_DIR = "./Network"
NETWORK_ID = 1234

INITIAL_BALANCE = "3000000000000000000"
GENESIS_FILE = f"{NETWORK_DIR}/Genesis.json" 

NETWORK_PARAMS={
    "node_dir" : NODE_DIR,
    "max_peer" : 50,
    "network_id" : NETWORK_ID,
    "monitoring" : {"ip":"127.0.0.1", "port":"3000", "id":"hello"},
    "influx_db" : {"ip":"10.19.12.59", "port":"8086", "db_name":"test"},
    "rpc" : {"ip":"127.0.0.1", "port":10000},
    "node" : {"port":30000},
}

def main():
    create_dir(NETWORK_DIR)

    # delete old data
    print("=== reset old data ===")
    reset = Reset(NODE_DIR)
    reset.reset()

    # Create new data folder
    print("=== create env folder ===")
    env = Env(NUM_OF_NODE, NODE_DIR)
    env.create()

    # Create Account
    print("=== create accounts ===")
    account = Account(NODE_DIR)
    account.create()

    # Init Geth(Genesis)
    print("=== init genesis ===")
    genesis = Genesis(GENESIS_FILE, NETWORK_ID, NODE_DIR, INITIAL_BALANCE)
    genesis.create_genesis_json(account.public_key_list)
    genesis.init_geth()

    # Create_network
    print("=== create network ===")
    network = Network(**NETWORK_PARAMS)
    network.create_network()

    # Validate network
    print("=== validate network ===")
    rpc_ip = NETWORK_PARAMS["rpc"]["ip"]
    w3 = Web3(HTTPProvider(f"http://{rpc_ip}:10000"))
    print(w3.net.peerCount)

if __name__ =="__main__":
    main()