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

    vm_output = connection.recv(65535)
    if re.search(b"% Invalid input", vm_output):
        print("There was at least one IOS syntax error on device {}".format(ip))
    else:
        print("Commands successfully executed on {}".format(ip))
        session.close()


if __name__ == "__main__":
    '''
        Main method of application
        establishing connection to virtual machine 
        Parameters:
         none
        Returns:
         none
     '''
    ssh_connection("192.168.147.128")
