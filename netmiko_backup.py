from getpass import getpass
from netmiko import ConnectHandler

addmore = 'y'

supported_platforms = ['cisco_ios', 'cisco_asa', 'cisco_xr', 'hp_procurve', 'juniper','arista_eos']

while True:

    devname = input("Device Hostname: ")

    #check if user input agrees with 'supported_platforms' list. If not, keep asking until it does.
    while True:
        devtype = input("Device Type (e.g. cisco_ios, arista_eos): ")
        if devtype in supported_platforms:
            break
        else:
            print("\nError! Unrecognised Platform.\nTry inserting one of the following: \n - cisco_ios\n - cisco_asa\n - cisco_xr\n - hp_procurve\n - juniper\n - arista_eos\n")

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

    
