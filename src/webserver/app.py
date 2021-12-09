# Manish Patel - CS 655
# GENI Mini Project - Web Page/Interface Code (using Flask)

from flask import Flask, render_template, request
import sys
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def interface():
    if request.method == 'POST':
        # These are the input fields that we get from the user filling out the form on the web interface. 
        hash_to_crack = request.form['hash']
        numWorkers = request.form['workers']

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        HOST = '130.127.215.156'
        PORTNUM = 2010
        # Connect our socket to the master node
        s.connect((HOST, PORTNUM))
        # Encode the hash to crack into bytes and send it over to the master node across the connection
        s.sendall(hash_to_crack.encode())
        # Store the response message (cracked password) from the master node, up to a maximum size of 1024 
        data = s.recv(1024)
        s.close()
    
    response = data.decode()
    # Render the form with the response from the master node included
    return render_template('form.html', cracked = response)


if __name__ == "__main__":
    app.run()
