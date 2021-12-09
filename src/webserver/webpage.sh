#!/bin/bash
wget https://raw.githubusercontent.com/mspatel927/cs655_passwordcracker/main/src/webserver/app.py
mkdir templates
cd templates
wget https://raw.githubusercontent.com/mspatel927/cs655_passwordcracker/main/src/webserver/templates/form.html
cd ..
app.py
