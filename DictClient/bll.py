"""

"""
import sys
from socket import *
from typing import Tuple

from request.get_def import GetDefinition
from request.get_history import GetHistory
from request.password import Password
from request.quit import Quit
from request.username import Username


class RequestController:

    def __init__(self, address):
        self.__c_socket = socket()
        self.__c_socket.connect(address)

    def handle_request(self, request: str) -> Tuple[bool, str]:
        """
            分情况组织请求
        :param request:
        :return: Y/N response
        """
        list_request = request.split(" ", 2)
        type = list_request[0]
        if type == "Q":
            return Quit().send_request(self.__c_socket)
        if type == "L":
            type = list_request[1]
            data = list_request[2]
            if type == "U":
                return Username().send_request(self.__c_socket, data)
            if type == "P":
                return Password().send_request(self.__c_socket, data)
        if type == "R":
            type = list_request[1]
            data = list_request[2]
            if type == "U":
                return Username().send_request(self.__c_socket, data)
            if type == "P":
                return Password().send_request(self.__c_socket, data)
        if type == "F":
            type = list_request[1]
            data = list_request[2]
            if type == "W":
                return GetDefinition().send_request(self.__c_socket, data)
            if type == "H":
                return GetHistory().send_request(self.__c_socket, data)
            sys.exit("程序退出")
        return (False, "异常")
