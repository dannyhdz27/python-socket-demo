import socket

host = socket.gethostname()
port = 12345

client_socket = socket.socket()
client_socket.connect((host, port))

message = "Hello from client!"
client_socket.send(message.encode())

data = client_socket.recv(1024).decode()
print("Received from server:", data)

client_socket.close()