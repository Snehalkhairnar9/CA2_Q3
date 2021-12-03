# File          : L00163434_Q3_File_2
# Author        : K. Snehal
# Version       : v1.0.0
# Licencing     : (C) 2021 Snehal Khairnar, LYIT
#                 Available under GNU Public License (GPL)
# Description   : Connection to Virtual machine
# ----------------------------------


import paramiko
import time
import re


# Open SSH connection to the device
# first install ssh-server on the VM
#           sudo apt install openssh-server openssh-client
#
def ssh_connection(ip):
    """
    """
    # try:
    username = "snehal"
    password = "Snehal@9"

    print("Establishing a connection...")
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(ip.rstrip("\n"), username=username, password=password)
    connection = session.invoke_shell()
    connection.send("ls -al > longList.txt\n")  # unix command to list directory contents and save to file
    time.sleep(1)

    vm_output = connection.recv(65535)
    if re.search(b"% Invalid input", vm_output):
        print("There was at least one IOS syntax error on device {}".format(ip))
    else:
        print("Commands successfully executed on {}".format(ip))
        session.close()


if __name__ == "__main__":
    # ssh_connection("192.168.37.144") #ip address of my VM, adjust to suit
    ssh_connection("192.168.147.128")
