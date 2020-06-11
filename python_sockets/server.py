import socket

UNIX_SOCKET_LOCATION = "./custom_socket"

new_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

new_socket.bind(UNIX_SOCKET_LOCATION)  # Bind server to socket

new_socket.listen()  # Server listens on given socket

while True:
    # Wait for a connection
    accepted_conn, client_addr = new_socket.accept()
    print(type(accepted_conn))
    print(accepted_conn)
    print(type(client_addr))
    print(client_addr)

    data = accepted_conn.recv(16)
    print(type(data))
    print(data.decode("UTF-8"))