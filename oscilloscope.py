import socket
from gpiozero import MCP3008
import time

analog = MCP3008(channel=0)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('0.0.0.0', 3000))
server_sock.listen(1)
while True:
	client_sock, addr = server_sock.accept()
	while True:
		analog_value = int(analog.value * 1024)
		client_sock.send(analog_value.to_bytes(2, 'big'))
		time.sleep(0.01)

