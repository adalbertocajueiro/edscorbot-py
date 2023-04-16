from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import server_api as api

UPLOAD_FOLDER = '/var/tmp'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    f = request.files['file']
    srcType = int(request.form['sourceType'])
    tgtType = int(request.form['targetType'])
    hasTimeInfo = request.form['hasTimeInfo'].lower() == "true"
    robotName = request.form['robotName']
    
    filename = secure_filename(f.filename)
    
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print('file ', file)
    f.save(file)
    outputFileName = api.convertNpy(file,srcType,tgtType,app.config['UPLOAD_FOLDER'],hasTimeInfo,robotName)
        
    return send_file(outputFileName, as_attachment=True)


if __name__ == '__main__':
    app.run(debug = True)