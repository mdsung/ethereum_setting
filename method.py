import os 
import subprocess
from shutil import rmtree

def create_directory(dir_name):
    if not validate_dir(dir_name):
        os.mkdir(dir_name)

def delete_directory(dir_name):
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

def run_command(cmd):
    popen = subprocess.Popen(cmd, shell=True)
    # popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # (stdoutdata, stderrdata) = popen.communicate()
    # return stdoutdata, stderrdata