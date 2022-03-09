import socket
from tkinter import filedialog

HOST = 'localhost' #coloca o host do servidor
PORT = 100

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))


s.send("Hello world".encode())
s.close()
