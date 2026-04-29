import socket

host = socket.gethostname()
port = 12345

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is waiting for connection...")

conn, address = server_socket.accept()
print("Connection from:", address)

data = conn.recv(1024).decode()
print("Received from client:", data)

conn.send("Hello from server!".encode())

conn.close()