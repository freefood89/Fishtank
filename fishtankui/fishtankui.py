from flask import Flask, request, render_template ,send_file, make_response, logging
import json
import calendar
import datetime

# import logging
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='templates/static')

SENSORS = ['a','b','c']
deviceControl = { "led1" : "Off" , "led2" : "Off", "led3" : "Off"};
sillyCache = dict()

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


@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    data = request.get_data()
    sillyCache['recentImage'] = bytearray(data)
    with open('test.jpeg','wb') as newFile:
            newFile.write(data)
    return 'Image Sent!'

@app.route('/recentImage')
def recentImage():
    if 'recentImage' in sillyCache:
        logger.debug('Image found in cache')
        response = make_response(sillyCache['recentImage'])
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['Content-Disposition'] = 'attachment; filename=recentImage.jpg'
        return response
    return send_file('test.jpeg',cache_timeout=1)

if __name__=='__main__':
    app.run(port=5000, debug=True)