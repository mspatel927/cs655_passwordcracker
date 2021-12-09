# Manish Patel - CS 655
# GENI Mini Project - Web Page/Interface Code (using Flask)

from flask import Flask, render_template, request
import sys
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def interface():
    if request.method == 'POST':
        hash_to_crack = request.form['hash']
        numWorkers = request.form['workers']

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     MASTER = '130.127.215.156'
    #     PORTNUM = 2010
    #     # Connect our socket to the specified server socket (based on the command line arguments above)
    #     s.connect((MASTER, PORTNUM))
    #     # Encode the string message into bytes and send it over to the server across the connection
    #     s.sendall(hash_to_crack.encode())
    #     # Store the response message from the server, up to a maximum size of 1024 
    #     data = s.recv(1024)
    #     s.close()
    
    # response = data.decode()
    response = "hello"


    return render_template('form.html', cracked = response)


if __name__ == "__main__":
    app.run()
