# Getting Started
This is the project containing the wrapper for the ED-Scorbot robotic arm to make it available
trought a REST API. This microservice is **strinctly** intended to provide end-points for users
interact directly with the robotic arm. 

In its architecture, the controller layer reuses a Python library with low level funcions to 
interact with the robotic arm. Therefore, this service is hosted at a computer connected
to the robotic arm trought USB. 

The service also implements features to handle que robot suitably such as, establishing the 
direct USB connection with the arm before any interaction with it, controlling all concurrent
access to the arm (if different users try to control the arm at the same time), moving the arm
to the home position before sending other commands to it, and so on. 

### ED-Scorbot Python Wrapper/Server
The server is a simple implementation. Before starting the server, install de dependencies:
* connexion (`pip install connexion`)
* logging (`pip install logging`)

### Files
* `edscorbot_webapi.py` - a simple server that puts the service running. This contains the high level
microservice and must be suitably *linked* with the loe level Python library. 
* `edscorbot_api.py` - this is a basic implementation of the Python library for direct interaction with the robotic arm. It also  contains comments regarding the features considered in its implementation. 
Currently, the implemented functions just contain *fake* bodies that return some value. As the project
evolves, these functions will be replaced with those from the real implementation, desirably using a low coupling architecture/patterns. 
* `swagger/escorbot.yaml` - the openapi documentation about the routes and the Web API. It also links the routes with the functions to be executed when invoked.

### Running instructions
* This simple server has been tested in Python 3.10.5 
* Type the command `python edscorbot_webapi.py` and the server should be up
* Make sure that the port 8080 is not in use
* To see and interact with the server use its Swagger by accessing http://localhost:8080/ui in your browser

### Extra information
* [Connexion](https://connexion.readthedocs.io/en/latest/routing.html) - information about the connexion library, used to implement the Web controller layer
* [Ed Scorbot Python] (https://github.com/RTC-research-group/Py-EDScorbotTool) - the Github projectcontaining the library (real implementation) of elementary/low level functions to access the robotic arm
* [Ed Scorbot Documentation] (https://py-edscorbottool.readthedocs.io/en/latest/) - the user documentation/guide of the ED Scorbot tools (GUI, command line and detailed configurations). 