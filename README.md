# Getting Started
This project contains a microservice for providing conversion support of files in NPY format into JSON. The microservice is **strinctly** used in the context of the EDScorbot to reduce the effort on manipulating NPY files externally before sending its content to the robotic arm in JSON or TSV format.

The service itself is a simple Flask server containing a single route that handle all conversions. 

The structure being convertes is a list/array of points, where each point is a list of coordinates. Ecah coordinate can be expressed in terms of angles (degrees or radians) or references (integer) to arm's joints. 

These types are represented by integer values:

* `1` for DEGREES
* `2` for RADIANS
* `3` for REFERENCES

The microservice is able to convert coordinate of a list of points from/to any of the above formats/types.

### Dependencies
Run these commands to install the dependencies if necessary:
* Flask (`pip install flask`)
* Flask CORS (`pip install flask_cors`)
* Werkzeug (`pip install werkzeug`)
* Numpy (`pip install numpy`)
* Json (`pip install json`)
* Datetime (`pip install datetime`)

### Files
* `server.py` - contains a simple server that launches the service on port 5000 (default por for Flask applications).
* `server_api.py` - contains the high level function implementing the conversion of NPY into JSON file. 
* `conversions.py` - the low level function implementations for converting coordinates among the types DEGREES, RADIANS and RERECENCES. For each robot, there are two functions: 
  - `angle_to_ref_ROBOTNAME` - a from angle (in radians) to reference value implementation for a specific robot
  - `ref_to_angle_ROBOTNAME` - a from reference value to angle (in radians) implementation for a specific robot
* `edscorbot.yaml` - the openapi specification of the microservice

### Running instructions
* This simple server has been tested in Python 3.10.5 
* Type the command `python server.py` and the server should be up
* Make sure that the port 5000 is not in use
* You can test the route `/python/convert` via POST method using tools like Postman or Insomnia

### Adding support to a new robotic arm
To add conversion support for a new robotic arm, you need to handle two specific files:
* `conversions.py` - this file contains the conversion functions specific to each robotic arm. You just have to create two funcions: `angle_to_ref_NEW_ROBOT_NAME` containing the body to convert one angle (given in radians as a double value) to reference value (integer) for each motor individually, and `ref_to_angle_NEW_ROBOT_NAME` containing the body to convert one reference value (integer) to an angle (in radians) returned as a double value. The following figure shows an example:

![Example of conversion function](/images/conversion-func-example.png "Example of conversion function")

To add conversion support to other robotic arm, add two new similar functions with other names to this file. 

* `server_api.py` - this file contains a map (`robotFunctionsMap` from robot name to an object containing two conversion functions: `angle_to_ref` and `ref_to_angle`). The object containing the conversion functions is represented as a map from function name to function definition. The following figure illustrates these structures for a specific robot("EDScorbot")

![Example of robot conversion functions](/images/robot-map.png "Example of map containing conversion functions for a specific robot")

To add conversion support to other robotic arm, add another element to the map `robotFunctionsMap` similarly to the existing one and reuse the suitable functions implemented in `conversions.py` 
    
### Extra information
* [Ed Scorbot Python] (https://github.com/RTC-research-group/Py-EDScorbotTool) - the Github project containing the library (real implementation) of elementary/low level functions to access the robotic arm
* [Ed Scorbot Documentation] (https://py-edscorbottool.readthedocs.io/en/latest/) - the user documentation/guide of the ED Scorbot tools (GUI, command line and detailed configurations). 