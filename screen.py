import socket
import matplotlib.pyplot as plt

CONNECT_HOST = '192.168.11.14'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((CONNECT_HOST, 3000))

data = []
plt.ion()

try:
	while True:
		recv_data = client_sock.recv(32)
		data.extend([int.from_bytes(recv_data[i:i+2], 'big') for i in range(0, 32, 2)])
		plt.plot(data)
		plt.pause(0.1)
except:
	pass

plt.ioff()
plt.show()