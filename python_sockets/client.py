import socket

UNIX_SOCKET_LOCATION = "./custom_socket"

new_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

new_socket.connect(UNIX_SOCKET_LOCATION)

while True:
    new_socket.sendall("Bok floki".encode("UTF-8"))