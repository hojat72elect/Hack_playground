import socket

"""
Here we have a simple echo server. It firstly creates a listening socket (a TCP socket) which 
is typical of a server. 

This socket connects to a specific host through a specific port. And after reading  
from that port, it will send all the received data into another socket."""

HOST = "127.0.0.1"
PORT = 65432

# This object is of type "socket" and is the default
# socket made for normal IP communications
basic_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Some common families of sockets are: AF_INET, AF_UNIX, AF_INET6, and ...
# In addition to that, various types of sockets are: SOCK_STREAM, SOCK_DGRAM,
# and so on...

# Bind the socket to an address. The socket must not already be bound.
# (The format of address depends on the address family) but we usually
# define it as a tuple of (host IP, local port)
basic_socket.bind((HOST, PORT))

# Prints out lots of important information abot the socket
print("The basic socket is: ", basic_socket)

# At this point, we have made a listening socket, which means it can listen to the other end.
basic_socket.listen()  # Just enables the socket to accept connections

# If the socket is already bound to an address and is listening to new connections, calling
# accept() will allow this socket to accept connections
connection_socket, connection_address = basic_socket.accept()

# connection_socket is a new socket object which is usable to send and receive data over this connection.
# connection_socket is non-inheritable.
print("the connection socket is", connection_socket)

print(f"The address of the connection is {connection_address}")

# send out all the received data from connection
while True:
    data = connection_socket.recv(1024)
    if not data:
        break
    connection_socket.sendall(data)
