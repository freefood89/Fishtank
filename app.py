from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from fishtankui.fishtankui import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8080,'0.0.0.0')
IOLoop.instance().start()
