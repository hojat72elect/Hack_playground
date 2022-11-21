import socket

"""
Here we have a simple echo server. It firstly creates a listening socket (a TCP socket) which 
is typical of a server. This socket connects to a specific host through a specific port. nd after reading  
from that port, it will send all the received data into another socket."""

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as default_socket:
    # create a listening socket; which is typical of what a server does.
    default_socket.bind((HOST, PORT))
    default_socket.listen()
    connection, address = default_socket.accept()
    print(f"The address of the connection is {address}")

    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
