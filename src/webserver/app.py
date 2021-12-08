# Manish Patel - CS 655
# GENI Mini Project - Web Page/Interface Code (using Flask)

from flask import Flask, render_template, request
import sys
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def interface():

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     # Connect our socket to the specified server socket (based on the command line arguments above)
    #     s.connect((HOST,PORTNUM))
    #     # Prompt the user to type out the message they want to send to the server and store it
    #     message = input("Enter your message: \n")
    #     # Print out the message that the client has typed and wants to send to the server
    #     print('Client sent', repr(message))
    #     # Encode the string message into bytes and send it over to the server across the connection
    #     s.sendall(message.encode())
    #     # Store the response message from the server, up to a maximum size of 1024 
    #     data = s.recv(1024)

    # # Print out the message (decoded back from bytes to string) that the server responded with (which here is the same as the sent messages)
    # print('Client received', repr(data.decode()))

    return render_template('form.html')


if __name__ == "__main__":
    app.run()
