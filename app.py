import socket

IP = "192.168.1.0"
PORT = 8080


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    s.send(b"Hello, world")
