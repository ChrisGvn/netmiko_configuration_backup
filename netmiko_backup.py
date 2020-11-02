from getpass import getpass
from netmiko import ConnectHandler

addmore = 'y'

while True:

    devname = input("Device Hostname: ")
    devtype = input("Device Type (e.g. cisco_ios, arista_eos): ")
    ip = input("IPv4 address of targeted device: ")
    ssh_u = getpass("SSH username: ")
    ssh_p = getpass("SSH password: ")
    enable = getpass("Enable password: ")

    device = { 
        'device_type':''+devtype+'',
        'ip':''+ip+'',
        'username':''+ssh_u+'',
        'password':''+ssh_p+'',
        'secret': ''+enable+''
    }
    
    net_conn = ConnectHandler(**device)
    net_conn.enable()
    configuration = net_conn.send_command('show run')

    with open(devname+'_config.txt', 'w') as configfile:
        configfile.write(configuration)

    addmore=input("Backup another configuration? (y/n): ")

    if addmore == 'y': 
        continue
    else: 
        break

    
