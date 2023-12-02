import socket
from threading import Thread
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port=9999

server.bind((ip_address, port))
server.listen()

list_of_clients = []
print("Server has started. ")

def clientThread(connection, address):
    connection.send("welcome to the chatroom". encode ("utf-8"))
    while True:
        try:
            message = connection.recv(1024).decode("utf-8")
            if message:
                print("<" + address[0] + ">" + message)

                message_to_send = "<" + address[0] + ">" + message
                broadcast(message_to_send, connection)
            else:
                remove(connection)
        except:
            continue

def broadcast (message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode("utf-8"))
            except:
                remove(clients)

def remove(connection):
    if connection != list_of_clients:
        list_of_clients.remove(connection)
        
while True:
    connection, address = server.accept()
    list_of_clients.append(connection)
    print(address[0]+ "connected....")
    new_thread = Thread(target=clientThread, args=(connection, address))
    new_thread.start()
# while True:
#     c,addrs = server.accept()
#     name = c.recv(1024).decode("utf-8")
#     print("Connection width: ",addrs, name)
#     c.send(bytes("welcome to my server", "utf-8"))
#     c.close()