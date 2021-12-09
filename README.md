# CS 655: GENI Mini Project - Password Cracker
This repo holds the code and instructions for the Password Cracker designed for the GENI Mini Project for CS 655. The code can be found in the src directory, and it is divided based on the 3 distinct parts of our architecture: the web server, the master node, and the worker node. 

The corresponding GENI slice for this project is located on the project labeled CS-655-Fall2021 and the slice is labeled PasswordCracker. The slice can be seen at the following URL: https://portal.geni.net/secure/slice.php?slice_id=3fd72465-f990-4ef0-9e20-592779e2a61c.

## Steps to Reproduce this Project
1. Access the XML file entitled `PasswordCracker_request_rspec` in this repo and use it to reserve resources on GENI using an InstaGENI site (Clemson InstaGENI was used for purposes of this project. ![alt text](https://github.com/mspatel927/cs655_passwordcracker/blob/main/resources_ready.PNG)
2. SSH into all of the nodes from the GENI topology, namely the master node and worker nodes 1, 2, 3, 4, and 5. 
3. On each of the worker nodes, run the included script to retrieve its necessary code and start running it. It is idenitifed by the worker node number. In other words, on worker node 2, you should run `worker2-init.sh` to do such. 
4. On the master node, run `masternode.sh` to retrieve the necessary code and start running it. 
5. On your local machine, run `webpage.sh` to retrieve the code for the web interface, create a directory for and save the template for the HTML form, and begin running the web server. 
6. At this point, the user can now go on the local host address where the web interface is located, access the HTML form, and type in the MD5 hash you wish to crack along with the number of worker nodes desired. ![alt text](https://github.com/mspatel927/cs655_passwordcracker/blob/main/web_interface.PNG)
7. Click submit, and after some period of time, the cracked password (if found) will appear at the bottom of the page. 
