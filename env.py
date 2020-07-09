from method import create_directory

class Env:
    def __init__(self, num_of_nodes, node_dir):
        self.num_of_nodes = num_of_nodes
        self.node_dir = node_dir
        self.dir_name_list = [str(i).zfill(5) for i in range(self.num_of_nodes + 1)]

    def create_parent_directory(self, node_dir):
        create_directory(node_dir)
    
    def create_child_directory(self, node_dir):
        for dir in self.dir_name_list:
            full_dir = f"{node_dir}/{dir}/"
            create_directory(full_dir)

    def create(self, node_dir):
        self.create_parent_directory(node_dir)
        self.create_child_directory(node_dir)
