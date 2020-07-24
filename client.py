import socket
import sys

def setup(host, port):
	# Create socket
	try:
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print("Created client socket.")
	except socket.error as err:
		print("Failed to create client socket: {}.".format(err))
		exit()

	return client_socket

def main():
	# Ask user for hostname and port
	# Note 127.0.0.1 is localhost
	host = raw_input("\nPlease input an internet domain or an IPv4 host address: ");
	port = raw_input("Please input a port number: ");

	if not port.isdigit():
		print("Invalid port number.")
		exit()

	client_socket = setup(host, int(port))

	# Send data
	message = raw_input("Please input a message to send to the host: ");
	client_socket.sendto(message, (host, int(port)));
	print("Sent: {}".format(message))

	# Close socket
	client_socket.close()
	exit()

main()
