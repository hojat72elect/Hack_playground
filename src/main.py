import socket

# a simple echo - server

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as defaultSocket:
    defaultSocket.bind((HOST, PORT))
    defaultSocket.listen()
    connection, address = defaultSocket.accept()
    print(f"The address of the connection is {address}")

    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
