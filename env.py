from method import create_dir

class Env:
    def __init__(self, num_of_nodes, node_dir):
        self.num_of_nodes = num_of_nodes
        self.node_dir = node_dir

    def create_parent_directory(self):
        create_dir(self.node_dir)
    
    def create_child_directory(self):
        dir_name_list = [str(i).zfill(5) for i in range(self.num_of_nodes + 1)]
        for dir in dir_name_list:
            full_dir = f"{self.node_dir}/{dir}/"
            create_dir(full_dir)

    def create(self):
        self.create_parent_directory()
        self.create_child_directory()
