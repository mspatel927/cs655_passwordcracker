# Manish Patel - CS 655
# GENI Mini Project - Worker Nodes code

import socket
import sys
import hashlib
import itertools

# The socket address of this worker node
HOST = '130.127.215.167'
PORTNUM = 2000

# Initialize our socket specifying the addressing scheme to be AF_INET (so we can use Internet addresses)
# and specifying the socket type to be SOCK_STREAM so that our data will transmit as a stream of characters
# Source: https://cis.temple.edu/~ingargio/old/cis307s96/readings/docs/sockets.html
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind this socket to this specific hostname/IP address and port number so that the master node can connect to it
    s.bind((HOST, PORTNUM))
    while True:
        # Allow the socket to wait for the master node to connect to it
        s.listen()
        # Accept the connection that arrives
        connection, address = s.accept()
        # Using this connection with the master node now...
        with connection:
            # Print out that we have now connected to the master node
            print('Connected by', address)
            # Start an infinite loop that takes in the data stream from the master node and break when there are no more bytes being sent
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                
                # Convert incoming bytes to usable string (password to crack)
                to_dehash = data.decode()
                
                # Our password can contain any character a-z and/or A-Z
                sample_space = "FGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDE"
                
                # Using these possible characters, iterate through every possible 5-character password
                # Infinite loop to brute force (loop forever until we find a match) 
                for possibility in itertools.product(sample_space, repeat=5):
                    # Find the MD5 hash of this password
                    attempt = ''.join(possibility)
                    hashed = hashlib.md5(attempt.encode('utf-8'))
                    hashed = hashed.hexdigest()

                    # Match found!
                    if hashed == to_dehash:
                        # This is the password cracked
                        cracked_password = attempt
                        break

                # Send the cracked password back to the master node
                connection.sendall(cracked_password.encode())



