import socket

host = '127.0.0.1'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

mensaje = str(input("Msj: "))
s.sendall(f'{mensaje}'.encode('utf-8'))
# resp = s.recv(1024).decode('utf-8')
# print(resp)
s.close()