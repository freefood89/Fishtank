Fishtank
========

Fishtank is a remote monitoring and control interface for my fishtank. The server is put together using the python [flask] framework.

##Starting Up the Servlet
You can easily start up the servlet raw using:
```bash
python3 hello.py
```
By launching the servlet in debug mode, you can edit the service without having to restart it everytime. This also turns on the logger in DEBUG mode.
```bash
python3 hello.py debug
```

##Starting Up Using Tornado
You can easily start up the servlet in a [tornado] container:
```bash
python3 tornadoTest.py
```
Launching via [tornado] will allow for simultaneous asynchronous connections by clients.

[flask]: (http://flask.pocoo.org/)
[tornado]: (http://www.tornadoweb.org/en/stable/)