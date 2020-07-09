import os
import sys
import psutil
import subprocess
from method import delete_directory

class Reset:
    TARGET_NAME = "geth"
    def kill_process(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if (proc.info["name"]) and (self.TARGET_NAME in proc.info["name"].lower()):
                process = psutil.Process(proc.info["pid"])
                process.kill()

    def del_node_dir(self, node_dir):
        delete_directory(node_dir)

    def reset(self, node_dir):
        self.kill_process()
        self.del_node_dir(node_dir)