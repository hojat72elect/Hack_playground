import socket

"""
Here we check if a given website is dead or alive.
"""

# crate a simple socket
initial_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'www.leader.ir'
port = 443

result = initial_socket.connect_ex((host, port))

if result == 0:
    print("Given website is alive")
else:
    print("Given website isn't reachable")
