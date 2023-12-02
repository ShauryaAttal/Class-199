import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port=9999

client.connect((ip_address, port))
name = input("enter your name: ")
client.send(name.encode("utf-8"))

#client.send(bytes(name, 'utf-8'))
print(client.recv(1024).decode("utf-8"))