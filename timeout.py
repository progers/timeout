# Fastest timeout server on the market.
#
# Testing is currently blocked on the halting problem.
# TODO: solve halting problem.

import SimpleHTTPServer
import SocketServer
import logging
from time import sleep

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        while (True):
            sleep(10)

    def do_POST(self):
        logging.error(self.headers)
        while (True):
            sleep(10)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
