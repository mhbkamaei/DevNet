from netmiko import ConnectHandler
from netmiko import SSHDetect

device = {
    "device_type": "cisco_ios",
    "host": "10.10.10.10",
    "username": "cisco",
    "password": "cisco"
}

ssh = ConnectHandler(**device)
print(ssh.find_prompt())
#print(con.send_command('show version'))
ssh.enable()
ssh.send_config_set('hostname switch2')
print(ssh.find_prompt())
ssh.disconnect()
