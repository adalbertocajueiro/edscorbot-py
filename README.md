# Getting Started

## ED-Scorbot Python Wrapper/Server
This is the project containing the wrapper for the ED-Scorbot robotic arm to make it available
trought a REST API. 

The server is a simple implementation. Before starting the server, install de dependencies:
* connexion (`pip install connexion`)
* logging (`pip install logging`)

## Files
* `edscorbot_webapi.py` - a simple server that puts the service running
* `edscorbot_api.py` - the (fake) library of functions for direct interaction with  the 
   robotic arm 
* `seagger/escorbot.yaml` - the openapi documentation about the routes and the Web API. It also links 
   the routes with the functions to be executed when invoked

## Running instructions
* This simple server has been tested in Python 3.10.5 
* Type the command `python edscorbot_webapi.py` and the server should be up
* Make sure that the port 8080 is not in use
* To see and interact with the server use its Swagger by accessing http://localhost:8080/ui in your browser

## Extra information
* Information about routing in connexion are available at https://connexion.readthedocs.io/en/latest/routing.html