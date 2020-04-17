"""

"""
from abc import abstractmethod
from socket import *


class Controller:

    def __init__(self, c_socket: socket):
        self.c_socket = c_socket

    @abstractmethod
    def handle_request(self) -> int:
        pass

    @abstractmethod
    def send_request(self, request: str) -> str:
        pass
