# Getting Started

## ED-Scorbot Python Wrapper/Server
This is the project containing the wrapper for the ED-Scorbot robotic arm to make it available
trought a REST API. 

The server is a simple file. Before starting the server, install de dependencies:
* connection
* logging

## Running instructions
* This simple server has been tested in Python 3.10.5 
* Type the command "python edscorbot-server.py" and the server should be up
* Make sure that the port 8080 is not in use
* To see and interact with the server use its Swagger by accessing http://localhost:8080/ui in your browser

## Extra information
* Information about routing in connexion are available at https://connexion.readthedocs.io/en/latest/routing.html