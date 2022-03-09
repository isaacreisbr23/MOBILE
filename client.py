import socket

target_host = 'localhost'
target_port = 1235

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send('Client Conectando ao server'.encode())
respose = client.recv(4096)
print(str(respose))
