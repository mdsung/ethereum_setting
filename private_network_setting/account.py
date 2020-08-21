import os 
from method import run_command, validate_file, validate_dir, write_file

class Account:
    def __init__(self, node_dir, network_dir):
        self.parent_dir = node_dir
        self.network_dir = network_dir
        self.child_dir_list = os.listdir(node_dir)

    def create_password_file(self):
        password = "password"
        write_file(self.password_file, password)

    def create_account(self):
        self.password_file = f"{self.network_dir}/password.txt"
        
        if not validate_file(self.password_file):
            self.create_password_file()

        for dir in os.listdir(self.parent_dir):
            cmd = f"""geth --datadir {self.parent_dir}/{dir} account new --password {self.password_file}"""
            run_command(cmd)

    def check_public_key(self):
        ## validate 한 후에 있으면 진행
        while True:
            flag = 0
            for child_dir in self.child_dir_list:
                dir_name = f"{self.parent_dir}/{child_dir}/keystore"
                if not validate_dir(dir_name):
                    continue
                if (len(os.listdir(dir_name)) > 0):
                    if ("tmp" not in os.listdir(dir_name)[0]):
                        flag += 1
            if flag == len(self.child_dir_list):
                break
            
    def create_public_key_list(self):
        self.check_public_key()            
        self.public_key_list = [os.listdir(f"{self.parent_dir}/{child_dir}/keystore")[0][-40:] for child_dir in self.child_dir_list]

    def create(self):
        self.create_account()
        self.create_public_key_list()
