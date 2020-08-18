import os
import sys
import psutil
import subprocess
from method import delete_dir, kill_process

class Reset:
    def __init__(self, node_dir):
        self.node_dir = node_dir

    def reset(self):
        kill_process("geth")
        delete_dir(self.node_dir)