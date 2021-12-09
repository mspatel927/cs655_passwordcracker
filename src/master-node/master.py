# Manish Patel - CS 655
# GENI Mini Project - Master Node code

import socket
import sys

# Use the first command line argument accepted to be the host name or IP address of the worker node
HOST_to_connect = str(sys.argv[1])      
# Use the second command line argument accepted to be the port number of the worked node
PORTNUM_to_connect = int(sys.argv[2])       

# The socket address of the master node itself
HOST = '130.127.215.156'
PORTNUM = 2010
HASH = ''

# Initialize our socket specifying the addressing scheme to be AF_INET (so we can use Internet addresses)
# and specifying the socket type to be SOCK_STREAM so that our data will transmit as a stream of characters
# Source: https://cis.temple.edu/~ingargio/old/cis307s96/readings/docs/sockets.html
# CONNECTION from the web interface to the master node 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind this socket to this specific hostname/IP address and port number so that the web interface can connect to it
    s.bind((HOST, PORTNUM))
    while True:
        # Allow the socket to wait for the web interface to connect to it
        s.listen()
        # Accept the connection that arrives
        connection, address = s.accept()
        # Using this connection with the app now...
        with connection:
            # Print out that we have now connected to the app
            print('Connected by', address)
            # Start an infinite loop that takes in the data stream from the app and break when there are no more bytes being sent
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                # The app sent over the hash that the user wants to crack
                HASH = data.decode()

                #--------------------------------------------------------------
                # CONNECTION from the master node to the worker nodes 
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    # Connect our socket to the specified worker socket (based on the command line arguments above)
                    sock.connect((HOST_to_connect,PORTNUM_to_connect))
                    # The message we'll send the workers is what the web interface sent the master node 
                    message = HASH
                    # Print out the message that the user has typed and wants to send to the workers to crack
                    print('Client sent', repr(message))
                    # Encode the string message into bytes and send it over to the workers across the connection
                    sock.sendall(message.encode())
                    # Store the response message from the workers, up to a maximum size of 1024 
                    data = sock.recv(1024)
                # A response means that the password has been cracked
                cracked_password = data.decode()
                # Print out the message (decoded back from bytes to string) that the worker responded with
                print('Client received', repr(cracked_password))
                #--------------------------------------------------------------

                # Send cracked password back to the web interface to be displayed
                connection.sendall(cracked_password.encode())
                s.close()
                break
        break

