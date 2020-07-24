import socket
import sys

def main():
	# Prompt user for port number
	print("\nThis program will be hosted on the localhost.")
	port = raw_input("Please input a port number: ");

	if not port.isdigit():
		print("Invalid port number.")
		exit()
	port = int(port)
	
	# Create socket
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Created server socket.")
	except socket.error as err:
		print("Failed to create server socket: {}.".format(err))
		exit()

	# Bind socket
	binding = ("localhost", port)
	serverSocket.bind(binding)
	print("Binded to port, {}. Waiting for connection.".format(port))

	# Listen for a connection
	serverSocket.listen(1)

	# Accept connection
	connection, client = serverSocket.accept()
	print("Connected.");

	# Receive data
	data = connection.recv(128)
	print("Received: {}".format(data))

	# Close socket
	serverSocket.close()
	exit()

main()
