# Getting Started
This is the project containing a microservice for providing conversion support of NPY files into JSON format.
This microservice is **strinctly** used in the context of the EDScorbot front-end to reduce the effort on manipulation NPY files externally before sending its content to the robotic arm in JSON or TSV format.

The service itself is a simple Flask server containing a single route. 

### Dependencies
Run these commands to install the dependencies if necessary:
* Flask (`pip install flask`)
* Flask CORS (`pip install flask_cors`)
* Werkzeug (`pip install werkzeug`)
* Numpy (`pip install numpy`)
* Json (`pip install json`)
* Datetime (`pip install datetime`)

### Files
* `server.py` - a simple server that puts the service running.
* `server_api.py` - the high level function implementing the conversion of NPY into JSON file. 
* `conversions.py` - the low level functions for converting coordiantes among the types DEGREES, RADIANS and RERECENCES.
* `edscobrot.yaml` - the openapi specification of the microservice

### Running instructions
* This simple server has been tested in Python 3.10.5 
* Type the command `python server.py` and the server should be up
* Make sure that the port 5000 is not in use
* You can test the route `/python/convert` via POST method using tools like Postman or Insomnia

### Adding characteristics of a new robotic arm

### Extra information
* [Ed Scorbot Python] (https://github.com/RTC-research-group/Py-EDScorbotTool) - the Github project containing the library (real implementation) of elementary/low level functions to access the robotic arm
* [Ed Scorbot Documentation] (https://py-edscorbottool.readthedocs.io/en/latest/) - the user documentation/guide of the ED Scorbot tools (GUI, command line and detailed configurations). 