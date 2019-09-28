"""
Author : Akshay Joshi
Created on 10-Sep-19
"""

from paramiko import *

ip = 'raspberrypi'
username = 'pi'
password = 'raspberry'
port = 22

cmds = [
        'echo "System Date : `date`"',
        'echo "System IP : `ip a | grep inet | grep -v inet6 | grep -v 127.0.0.1 | cut -d" " -f 6 | cut -d"/" -f1`"',
        'echo "Raspberry Pi CPU Temperature : `vcgencmd measure_temp | cut -d= -f2`"',
        ]

full_op_dump = ""

# Create SSH Object
ssh = SSHClient()
# Adding missing host key policy
ssh.set_missing_host_key_policy(AutoAddPolicy)
ssh.connect(ip, port, username, password)
for cmd in cmds:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    outline = stdout.readlines()
    outline = ' '.join(outline)
    #print (outline)
    full_op_dump = full_op_dump + "\n" + outline
print(full_op_dump)
ssh.close()