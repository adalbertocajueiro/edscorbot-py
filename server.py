from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import server_api as api

UPLOAD_FOLDER = '/var/tmp'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=['GET'])
def hello():
    return 'Hello'

@app.route('/convert' , methods = ['POST'])
def convertFile():
    """
        It converts a EDScorbot NPY file in JSON format. The NPY file contains an array of arrays (N-dimensional)
        containing points (a tuple of coordinates). The value N depends of the number of joints of each arm.
        Depending on the target type, it applies transformation functions between the source and the target types.
        These functions are defined for each arm. the types can be DEGREES (1), RADIANS(2) REFS(3) and COUNTERS(4)

        :return: a JSON containing all points of the arm with a specific target type
    """
    f = request.files['file']
    srcType = int(request.form['sourceType'])
    tgtType = int(request.form['targetType'])
    
    #filename = secure_filename(f.filename)
    filename = secure_filename(f.filename)
    
    #f.save(filename)
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print('file ', file)
    f.save(file)
    outputFileName = api.convertNpy(file,srcType,tgtType,app.config['UPLOAD_FOLDER'])
        
    return send_file(outputFileName, as_attachment=True)


if __name__ == '__main__':
    app.run(debug = True)