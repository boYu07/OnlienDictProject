"""
    请求接口
"""
from abc import abstractmethod
from socket import *

class Request:

    @abstractmethod
    def send_request(self, c_socket: socket, request=""):
        pass
