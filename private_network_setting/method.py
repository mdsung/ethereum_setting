import os 
import subprocess
import psutil
from shutil import rmtree

def create_dir(dir_name):
    if not validate_dir(dir_name):
        os.mkdir(dir_name)

def delete_dir(dir_name):
    if validate_dir(dir_name):
        rmtree(dir_name)

def validate_file(file_name):
    return os.path.isfile(file_name)

def validate_dir(dir_name):
    return os.path.isdir(dir_name)

def read_file(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    return content 

def write_file(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)

def run_command(command):
    p = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines = True)
    
def kill_process(target_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if (proc.info["name"]) and (target_name in proc.info["name"].lower()):
            process = psutil.Process(proc.info["pid"])
            process.kill()
