import os 
from method import read_file, write_file, run_command, validate_file

class Genesis:
	def __init__(self, genesis_file, network_id, node_dir, initial_balance):
		self.genesis_file = genesis_file
		self.node_dir = node_dir
		self.initial_balance = initial_balance
		self.genesis = f"""
{{
	"config": {{
	  "chainId": {network_id},
	  "homesteadBlock": 0,
	  "eip150Block": 0,
	  "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
	  "eip155Block": 0,
	  "eip158Block": 0,
	  "byzantiumBlock": 0,
	  "constantinopleBlock": 0,
	  "petersburgBlock": 0,
	  "istanbulBlock": 0,
	  "ethash": {{}}
	}},
	"nonce": "0x0",
	"timestamp": "0x5e4a53b2",
	"extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
	"gasLimit": "0x47b760",
	"difficulty": "0x80000",
	"mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
	"coinbase": "0x0000000000000000000000000000000000000000",
	"alloc": {{
		alloc_string
	}},
	"number": "0x0",
	"gasUsed": "0x0",
	"parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
  }}
"""
	def fill_genesis_json(self, publickeylist):
		alloc_string = ",\n\t\t".join([f'"{key}":{{"balance":\"{self.initial_balance}\"}}' for key in publickeylist])
		self.genesis = self.genesis.replace("alloc_string", alloc_string)
    
	def create_genesis_json(self, publickeylist):
		self.fill_genesis_json(publickeylist)
		write_file(self.genesis_file, self.genesis)
    
	def init_geth(self):
		for dir in os.listdir(self.node_dir):
			command = f"geth --datadir {self.node_dir}/{dir} init {self.genesis_file}"
			run_command(command)
    
