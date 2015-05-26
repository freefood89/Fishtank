from flask import Flask, request, render_template ,send_file, make_response, logging, jsonify
import flask
import json
import calendar
import datetime
import io
import os.path
import re
from PIL import Image
from fishtankui.exceptions import ApiException

logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='templates/static')

SENSORS = ['a','b','c']
deviceControl = { "led1" : "Off" , "led2" : "Off", "led3" : "Off"};
sillyCache = dict()

@app.errorhandler(ApiException)
def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def home_page():
    # logger.info('entered handler')
    return render_template('index.html')

@app.route('/dashboard/')
def show_dashboard():
    return render_template('dashboard/index.html', buttons=deviceControl.keys())

@app.route('/sensors/<sensor_id>')
def sensor_data(sensor_id):
    data = {}
    numResults = 1
    params = request.args.to_dict()
    if not params['t']:
        return 404

    now = calendar.timegm(datetime.datetime.now().timetuple())*1000
    print(now)

    data["oxygen"]=[]
    for post in collection.find({"date":{"$lt":now,"$gt":now-2000000}}):
        print(post)
        data["oxygen"].append([post["date"],post["oxygen"]])
        ##print(collection.find({"date":{"$lt":now,"$gt":now-2000000}}).count())

    print(data)
    return json.dumps(data)

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html')

def log_user_in(name):
    return 'Welcome'+name

def valid_login(username, password):
    print((username, password))
    return True

@app.route('/devices/<device_id>/toggle', methods=['PUT'])
def toggle(device_id):
    if not device_id in deviceControl:
        return ("Device " + device_id + " does not exist",404)
    if deviceControl[device_id] == 'Off':
        deviceControl[device_id] = 'On'
    else:
        deviceControl[device_id] = 'Off'
    return ("Success",202)

@app.route('/devices/<device_id>')
def state(device_id):
    if device_id == "~":
        return json.dumps(deviceControl)
    elif not device_id in deviceControl:
        return ("Device " + device_id + " does not exist",404)
    return deviceControl[device_id]

@app.route('/devices', methods=['GET'])
def deviceList():
    return json.dumps([i for i in deviceControl.keys()])

@app.route('/images/<filename>')
def getImage(filename):
    if filename in sillyCache:
        logger.debug('Image found in cache')
        response = make_response(sillyCache[filename])
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
    try:
        return send_file(filename,cache_timeout=1)
    except FileNotFoundError:
        raise ApiException('Image Not Found', 404)

@app.route('/images', methods=['POST'])
def handleImage():
    if 'Content-Type' not in request.headers:
        raise ApiException('Missing Required Headers', 400, culprit='Content-Type not specified')
    elif request.headers['Content-Type'].split('/')[0] != 'image':
        raise ApiException('Invalid Required Headers', 400, culprit='Content-Type invalid')
    
    if 'Content-Disposition' not in request.headers:
        raise ApiException('Missing Required Headers', 400, culprit='Content-Disposition not specified')
    elif re.search(request.headers['Content-Disposition'], r'filename=(\w+\.\w+)'):
        raise ApiException('Invalid Required Headers', 400, culprit='Content-Disposition invalid')

    request.headers['Content-Type']

    try:
        image = Image.open(io.BytesIO(bytearray(request.get_data())))
    except IOError:
        raise ApiException('Image Not Created', 400, culprit='Corrupt Image')

    logger.debug(request.headers['Content-Disposition'])
    # sillyCache[] = image
    try:
        image.save('test.jpg')
        return flask.Response(status=201)
    except Exception as e:
        raise ApiException('Image Not Created', 401)

if __name__=='__main__':
    app.run(port=5000, debug=True)