"""

"""
from socket import socket

from request.abs_request import Request


class FindR(Request):

    def __init__(self, c_socket: socket, db):
        super().__init__(c_socket, db)

    def do_request(self, request):
        pass

    def send_response(self):
        pass
