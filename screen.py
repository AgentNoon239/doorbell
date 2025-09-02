import socket
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import time
import os

CONNECT_HOST = '25.8.249.240'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((CONNECT_HOST, 3000))

data = []
plot_counter = 0

try:
	while True:
		recv_data = client_sock.recv(32)
		data.extend([int.from_bytes(recv_data[i:i+2], 'big') for i in range(0, 32, 2)])
		
		# Clear the current figure and plot new data
		plt.clf()
		plt.plot(data)
		plt.title(f'Real-time Data Plot - Sample {len(data)}')
		plt.xlabel('Sample Index')
		plt.ylabel('Value')
		
		# Save the plot to a file
		filename = f'plot_{plot_counter:04d}.png'
		plt.savefig(filename, dpi=100, bbox_inches='tight')
		print(f"Saved plot: {filename}")
		
		plot_counter += 1
		time.sleep(0.1)  # Small delay instead of plt.pause()
		
except KeyboardInterrupt:
	print("Stopping data collection...")
except Exception as e:
	print(f"Error: {e}")
finally:
	client_sock.close()
	print("Connection closed.")