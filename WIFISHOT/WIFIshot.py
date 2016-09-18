import PIL
import ImageGrab
import socket
import io
import atexit


def server():
	while True:
		print('wait..')
		conn, addr = server_socket.accept()
		if conn:
			print(conn)
			print(addr)
			connection = conn.makefile('wb')
			break
	print('connecting..')
	try:
		stream = io.BytesIO()
		ImageGrab.grab().save('1.jpg','JPEG')
		stream.write(io.FileIO('1.jpg','r').readall())
		stream.seek(0)
		connection.write(stream.read())
		stream.seek(0)
		stream.truncate()
	finally:
		print('close connection...')
		connection.close()
		
def onExit():
	connection.close()
	server_socket.close()
	print('exit')

	
server_socket = socket.socket()
server_socket.bind(('0.0.0.0',8000))
server_socket.listen(0)
server_socket.setblocking(1)

while True:
	server()