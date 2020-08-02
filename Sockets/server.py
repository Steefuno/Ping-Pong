import signal
import socket
import sys

def setup(port):
	global server_socket

	# Create socket
	try:
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print("Created server socket.")
	except socket.error as err:
		print("Failed to create server socket: {}.".format(err))
		exit()

	# Bind socket
	binding = ("localhost", port)
	server_socket.bind(binding)
	print("Binded to port, {}. Waiting for connection.".format(port))

def terminate(signalNumber, frame):
	server_socket.close()
	print("Closed server socket.")
	exit()

def main():
	# Prompt user for port number
	print("\nThis program will be hosted on the localhost.")
	port = input("Please input a port number: ")

	if no	t port.isdigit():
		print("Invalid port number.")
		exit()

	setup(int(port))

	# register terminate signals
	signal.signal(signal.SIGINT, terminate)

	while True:
		print("Waiting for message.")
		message, address = server_socket.recvfrom(4096)
		print("Received message from {}.".format(address))
		print(message)

	print("Hey.")

main()
