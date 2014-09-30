from flask import Flask, request, render_template
app = Flask(__name__)

LEDControl = {};

@app.route('/')
def hello_world():
    return 'Hello World!'

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


@app.route('/feed', methods=['POST','GET'])
def feed():
    LEDControl['LED State'] = 'On'

@app.route('/toggle', methods=['POST'])
def toggle():
    LEDControl['LED State'] = 'Off'
    return 'hello_world'

@app.route('/state', methods=['POST','GET'])
def state():
    return LEDControl['LED State']

if __name__ == '__main__':
    app.run(host='0.0.0.0')
