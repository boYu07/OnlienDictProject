"""
    服务端 请求解析
"""
import sys
from socket import *

from request.insert import Insert
from request.select import Select


class RequestController:

    def __init__(self, c_socket: socket, database):
        self.__c_socket = c_socket
        self.__database = database
        self.__cursor = self.__database.cursoe()

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
        list_data = request.decode().split(" ", 2)
        print(list_data)  # debug
        return list_data

    def handle_request(self):
        """
            解析请求请求
        """
        while True:
            list_data = self.__analyze_request()
            request_type = list_data[0]
            if request_type == "L":
                # 登录请求
                if list_data[1] == "U":
                    # 插入请求
                    handler = Insert(self.__database)
                    response = handler.do_request([list_data[2]],
                                                  "username",
                                                  "user")
                    if response == 0:
                        self.__c_socket.send(b"N")

                if list_data[1] == "P":
                    # 密码请求
                    pass
                continue
            if request_type == "R":
                # 注册请求
                if list_data[1] == "U":
                    # 查询请求
                    pass
                if list_data[1] == "P":
                    # 密码请求
                    pass
                continue
            if request_type == "F":
                # 查询请求
                if list_data[1] == "W":
                    # 解释请求
                    pass
                    continue
                if list_data[1] == "H":
                    # 历史请求
                    pass
                continue
            print("未知请求")
