from web3 import Web3, HTTPProvider

class Node:
    def __init__(self, blockchain_ip, node):
        self.w3 = Web3(HTTPProvider(f"http://{blockchain_ip}:{10000+node}"))

class Transaction:
    def __init__(self, blockchain_ip, from_node, to_node):
        self.blockchain_ip = blockchain_ip
        self.from_node = Node(blockchain_ip, from_node)
        self.to_node = Node(blockchain_ip, to_node)

        self.from_w3 = self.from_node.w3
        self.to_w3 = self.to_node.w3

        self.from_account = self.from_w3.geth.personal.listAccounts()[0]
        self.to_account = self.to_w3.geth.personal.listAccounts()[0]

        self.tx = self.from_w3.eth.sendTransaction
        self.unlockAccounts()

        self.transaction_history = []

    def unlockAccounts(self):
        self.from_w3.geth.personal.unlockAccount(self.from_account, 'password')
        
    def stringtoHex(self, string):
        return string.encode('utf-8').hex()

    def transact(self, value, data):
        transaction = self.tx({'to': self.to_account, 
                        'from': self.from_account, 
                        'value': value, 
                        'data' : self.stringtoHex(data)})
        self.transaction_history.append(transaction)
    
    @staticmethod
    def get_input_data(blockchain_ip, txHash):
        n = Node(blockchain_ip, 0)
        input_data = n.w3.eth.getTransaction(txHash)["input"][2:]
        return bytes.fromhex(input_data).decode('UTF-8')
