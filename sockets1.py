"""This class show how use socket commands"""
import socket

mySocket = socket.socket()
mySocket.connect(("127.0.0.1",445))
resp = mySocket.recv(0)
print(resp)
mySocket.close()