# Manish Patel - CS 655
# GENI Mini Project - Worker Nodes code

import socket
import sys
import hashlib
import itertools

# HOST = '127.0.0.1'
# Set the host address to 0.0.0.0 so that it can encompass all IP addresses on the local machine
HOST = '0.0.0.0'
# Use the second command line argument accepted to be the port number that this server will run on 
PORTNUM = int(sys.argv[1])

# Initialize our socket specifying the addressing scheme to be AF_INET (so we can use Internet addresses)
# and specifying the socket type to be SOCK_STREAM so that our data will transmit as a stream of characters
# Source: https://cis.temple.edu/~ingargio/old/cis307s96/readings/docs/sockets.html
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind this socket to this specific hostname/IP address and port number so that the client can connect to it
    s.bind((HOST, PORTNUM))
    # Start an infinite loop so that until we forcefully shut down the server, clients can continue to connecto the server 
    while True:
        # Allow the socket to wait for any clients to connect to it
        s.listen()
        # Accept a client connection that arrives
        connection, address = s.accept()
        # Using this connection with the client now...
        with connection:
            # Print out that we have now connected to a specific client
            print('Connected by', address)
            # Start an infinite loop that takes in the data stream from the client and break when there are no more bytes being sent
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                
                # Convert incoming bytes to usable string (password to crack)
                to_dehash = data.decode()
                
                # Our password can contain any character a-z and/or A-Z
                sample_space = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
                # Using these possible characters, iterate through every possible 5-character password
                # Infinite loop to brute force (loop forever until we find a match) 
                for possibility in itertools.product(sample_space, repeat=5):
                    # Find the MD5 hash of this password
                    hashed = hashlib.md5(possibility.encode('utf-8'))
                    hashed = hashed.hexdigest()

                    # Match found!
                    if hashed == to_dehash:
                        # This is the password cracked
                        cracked_password = possibility
                        break

                # Send all the data we just received back to the client, to "echo" its sent message 
                connection.sendall(cracked_password.encode())



