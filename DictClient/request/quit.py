"""

"""
import sys
from socket import socket

from request.request import Request


class Quit(Request):

    def send_request(self, c_socket: socket, request=""):
        c_socket.send(b"Q")
        c_socket.close()
        sys.exit("客户端退出")
