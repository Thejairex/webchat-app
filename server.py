import socket
import select


host = '127.0.0.1'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen()

sockets_list = [server_socket]
clients = {}


while True:
	read_socket, _, _ = select.select(sockets_list, [], [])

	for sock in read_socket:
		if sock == server_socket:
			client_socket , client_address = server_socket.accept()
			sockets_list.append(client_socket)
			clients[client_socket] = client_address
			print(f'Nueva conexion desde {client_address[0]}:{client_address[1]}')

		else:

			try:
				data = sock.recv(1024)
				if data:
					print('Datos recibidos de', clients[sock], ':', data.decode('utf-8'))

				else:
					print(f'Desconexion de: {client_address[0]}:{client_address[1]}')
					sockets_list.remove(sock)
					del clients[sock]

			except ConnectionResetError:
				print('El cliente', clients[sock], 'cerró el programa forzosamente.')
				sockets_list.remove(sock)
				del clients[sock]

		print('clientes conectados: ', [clients[sock] for sock in clients])



			# message = sock.recv(1024)
			# if not message:
			# 	sockets_list.remove(sock)
			# 	print(f'Desconexion de: {client_address[0]}:{client_address[1]}')
			# 	continue
			# print(f'message recibido: {message.decode("utf-8")}')