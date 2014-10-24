from flask import Flask, request, render_template , send_file
import json
import random

app = Flask(__name__)
SENSORS = ['a','b','c']
LEDControl = {'LED State':'Off'};

@app.route('/')
def hello_world():
    return 'Welcome to the Fish. Tank.!'

@app.route('/sensor/<sensor_id>/')
def sensor_data(sensor_id):
    print('entered')
    data = {}
    numResults = 1
    params = request.args.to_dict()
    print(params)
    if params['n'] and int(params['n'])>0 and int(params['n'])<21:
        numResults = int(params['n'])
    print(sensor_id, numResults)
    data[sensor_id] = [random.randint(1,10) for x in range(1,numResults)]
    print(data)
    return json.dumps(data)

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')

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

@app.route('/toggle', methods=['POST'])
def toggle():
    if LEDControl['LED State'] == 'Off':
        LEDControl['LED State'] = 'On'
    else:
        LEDControl['LED State'] = 'Off'
        return 'LED State is now whatever the fuck you wanted'

@app.route('/feed', methods=['POST'])
def feed():
    if request.method == 'POST':
        return toggle()

@app.route('/state', methods=['POST','GET'])
def state():
    return LEDControl['LED State']

@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    data = request.get_data()
    newFileByteArray = bytearray(data)
    with open('test.jpeg','wb') as newFile:
            newFile.write(data)
    return 'Image Sent!'

@app.route('/recentImage')
def recentImage():
     return send_file('test.jpeg', mimetype='image/gif')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
