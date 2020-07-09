import os 
from method import read_file, write_file, run_command, validate_file

class Genesis:
    INITIAL_BALANCE = "3000000000000000000"
    GENESIS_TEMPLATE = """
{
	"config": {
	  "chainId": 1234,
	  "homesteadBlock": 0,
	  "eip150Block": 0,
	  "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
	  "eip155Block": 0,
	  "eip158Block": 0,
	  "byzantiumBlock": 0,
	  "constantinopleBlock": 0,
	  "petersburgBlock": 0,
	  "istanbulBlock": 0,
	  "ethash": {}
	},
	"nonce": "0x0",
	"timestamp": "0x5e4a53b2",
	"extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
	"gasLimit": "0x47b760",
	"difficulty": "0x80000",
	"mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
	"coinbase": "0x0000000000000000000000000000000000000000",
	"alloc": {
		account
	},
	"number": "0x0",
	"gasUsed": "0x0",
	"parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
  }
"""
    def __init__(self,genesis_template_file, genesis_file):
        self.genesis_template_file = genesis_template_file
        self.genesis_file = genesis_file
    
    def create_genesis_template_file(self):
        write_file(self.genesis_template_file, self.GENESIS_TEMPLATE)

    def fill_genesis_json(self, publickeylist):
        alloc_string = ",\n\t\t".join([f'"{key}":{{"balance":\"{self.INITIAL_BALANCE}\"}}' for key in publickeylist])
        self.genesis = self.genesis.replace("account", alloc_string)
    
    def create_genesis_json(self, publickeylist):
        if not validate_file(self.genesis_template_file):
            self.create_genesis_template_file()
        self.genesis = read_file(self.genesis_template_file)
        self.fill_genesis_json(publickeylist)
        write_file(self.genesis_file, self.genesis)
    
    def init_geth(self, node_dir):
        for dir in os.listdir(node_dir):
            command = f"""geth --datadir {node_dir}/{dir} init {self.genesis_file}"""
            run_command(command)
    
