import socket
import sys

def main():
	# Ask user for hostname and port
	# Note 127.0.0.1 is a localhost
	host = raw_input("\nPlease input an internet domain or an IPv4 host address: ");
	port = raw_input("Please input a port number: ");

	if not port.isdigit():
		print("Invalid port number.")
		exit()
	port = int(port)
	
	# Create socket
	try:
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Created client socket.")
	except socket.error as err:
		print("Failed to create client socket: {}.".format(err))
		exit()

	# Connect socket to server's bind
	binding = (host, port)
	clientSocket.connect(binding)
	print("Binded client socket to host, {}, at port, {}.".format(host, port))

	# Send data
	message = raw_input("Please input a message to send to the host: ");
	clientSocket.send(message.encode("utf-8"))
	print("Sent: {}".format(message))

	# Close socket
	clientSocket.close()
	exit()

main()
