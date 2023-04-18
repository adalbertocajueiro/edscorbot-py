from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import server_api as api
import numpy as np

UPLOAD_FOLDER = '/var/tmp'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/python/load' , methods = ['POST'])
def loadFile():
    """
    It loads the content of a NPY file and returns it as a json without any modification. 
    :return: a JSON containing all points of the arm with a specific target type
    """
    f = request.files['file']
    filename = secure_filename(f.filename)
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(file)
    arr = np.load(file)
    list = arr.tolist()

    data = {'content':list}
    
    return jsonify(data)  
    
@app.route('/python/convert' , methods = ['POST'])
def convertFile():
    """
    It converts a EDScorbot NPY file in JSON format. The NPY file contains an array of arrays (N-dimensional)
    containing points. Each point is a tuple of coordinates with three possible types: angles in DEGREES(1),
    angles in RADIANS(2) or REFERENCE VALUES(3). If a waiting time information is present in the last 
    coordinate, the conversion is applied to all previous points. Otherwise, the conversion is applied
    to all points.

    :return: a JSON containing all points of the arm with a specific target type
    """
    list = request.form['content']
    srcType = int(request.form['sourceType'])
    tgtType = int(request.form['targetType'])
    hasTimeInfo = request.form['hasTimeInfo'].lower() == "true"
    robotName = request.form['robotName']
    
    convertedList = api.convertNpy(list,srcType,tgtType,hasTimeInfo,robotName)
    
    data = {'content':convertedList}
    
    return jsonify(data)  


if __name__ == '__main__':
    app.run(debug = True)