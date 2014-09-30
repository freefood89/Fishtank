from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from hello import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8001)#80,'0.0.0.0')
IOLoop.instance().start()
