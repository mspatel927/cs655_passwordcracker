# Manish Patel - CS 655
# GENI Mini Project - Master Node code

import socket
import sys

# Use the first command line argument accepted to be the host name or IP address of the server we want to connect to
HOST_to_connect = str(sys.argv[1])      
# Use the second command line argument accepted to be the port number of the server we want to connect to
PORTNUM_to_connect = int(sys.argv[2])       

HOST = '130.127.215.156'
PORTNUM = 2010

HASH = ''
# Initialize our socket specifying the addressing scheme to be AF_INET (so we can use Internet addresses)
# and specifying the socket type to be SOCK_STREAM so that our data will transmit as a stream of characters
# Source: https://cis.temple.edu/~ingargio/old/cis307s96/readings/docs/sockets.html
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind this socket to this specific hostname/IP address and port number so that the client can connect to it
    s.bind((HOST, PORTNUM))
    # Start an infinite loop so that until we forcefully shut down the server, clients can continue to connect to the server 
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
                HASH = data.decode()
                s.close()
                break
        break



# Initialize our socket specifying the addressing scheme to be AF_INET (so we can use Internet addresses)
# and specifying the socket type to be SOCK_STREAM so that our data will transmit as a stream of characters
# Source: https://cis.temple.edu/~ingargio/old/cis307s96/readings/docs/sockets.html
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect our socket to the specified server socket (based on the command line arguments above)
    s.connect((HOST_to_connect,PORTNUM_to_connect))
    # Prompt the user to type out the message they want to send to the server and store it
    message = HASH
    # Print out the message that the client has typed and wants to send to the server
    print('Client sent', repr(message))
    # Encode the string message into bytes and send it over to the server across the connection
    s.sendall(message.encode())
    # Store the response message from the server, up to a maximum size of 1024 
    data = s.recv(1024)

# Print out the message (decoded back from bytes to string) that the server responded with (which here is the same as the sent messages)
print('Client received', repr(data.decode()))
