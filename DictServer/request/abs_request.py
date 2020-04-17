"""
    请求接口
"""
from abc import abstractmethod
from socket import *


class Request:

    def __init__(self, c_socket: socket, db):
        self.c_socket = c_socket
        self.db = db
        self.cursor = self.db.cursor()

    @abstractmethod
    def do_request(self, request):
        pass
