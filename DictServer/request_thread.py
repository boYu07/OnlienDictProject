"""
    自定义线程类
"""
import sys
from socket import *
from threading import Thread

from request.sign_in import SignInR
from request.sign_on import SignOnR


class RequestThread(Thread):

    def __init__(self, c_socket: socket, db):
        super().__init__()
        self.__c_socket = c_socket
        self.__db = db
        self.__controller = None

    def __analyze_request(self):
        """
            解析请求
        """
        request = self.__c_socket.recv(1024)
        print(request)
        if not request or request == b"Q":
            print("已退出")
            self.__c_socket.close()
            sys.exit("已退出")
        return request.decode().split(" ", 2)

    def __handle_request(self):
        """
            解析请求请求
        """
        while True:
            list_request = self.__analyze_request()
            print(list_request)  # debug
            request_type = list_request[0]
            if request_type == "L":
                self.__controller = SignInR(self.__c_socket, self.__db)
                self.__controller.do_request(list_request)
                continue
            if request_type == "R":
                self.__controller = SignOnR(self.__c_socket, self.__db)
                self.__controller.do_request(list_request)
                continue
            if request_type == "F":
                self.__controller = FindR()
            if request_type == "H":
                # 历史请求
                pass
                continue
            print("未知请求", list_request)

    def run(self) -> None:
        self.__handle_request()
