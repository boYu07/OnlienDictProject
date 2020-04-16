"""
    自定义线程类
"""
from socket import *
from threading import Thread

from request_controller import RequestController


class RequestThread(Thread):

    def __init__(self, c_socket: socket, database):
        super().__init__()
        self.__c_socket = c_socket
        self.__controller = RequestController(database)

    def run(self) -> None:
        data = self.__c_socket.recv(1024)
        if not data:
            print("已退出")
            self.__c_socket.close()
            return
        self.__controller.handle_request(data)
