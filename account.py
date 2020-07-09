import os 
from method import run_command, validate_file

class Account:
    def __init__(self, node_dir):
        self.parent_dir = node_dir
        self.child_dir_list = os.listdir(node_dir)

    def create_password_file(self):
        password = "password"
        with open(self.password_file, "w") as f:
            f.write(password)

    def create_account(self):
        self.password_file = "./Network/password.txt"
        
        if validate_file(self.password_file):
            self.create_password_file()

        for dir in os.listdir(self.parent_dir):
            cmd = f"""geth --datadir {self.parent_dir}/{dir} account new --password {self.password_file}"""
            run_command(cmd)

    def create_public_key_list(self):
        self.public_key_list = [os.listdir(self.parent_dir + "/" + child_dir + "/keystore")[0][-40:] for child_dir in self.child_dir_list]

    def create(self):
        self.create_account()
        self.create_public_key_list()
