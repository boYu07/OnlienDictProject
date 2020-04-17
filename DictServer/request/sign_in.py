"""

"""
from socket import socket
from typing import List

from request.abs_request import Request


class SignInR(Request):

    def __init__(self, c_socket: socket, db):
        super().__init__(c_socket, db)
        self.__username = ""

    def do_request(self, request: List[str]):
        """
            处理请求
        :param request: ["L", "username password"]
        """
        username, password = request[1].split(" ")
        # 插入请求
        response = self.__is_available(username, password)
        if not response:
            self.c_socket.send(b"N")
            return
        self.c_socket.send(b"Y")
        self.__username = username

    def __is_available(self, *args) -> bool:
        """
            查询
        :return: 查到 True, 查询不到 False
        """
        print(args)
        sql = "select username from user where username = %s and password = %s;"
        self.cursor.execute(sql, args)
        if self.cursor.fetchone():
            return True
        return False

    def get_u_id(self) -> int:
        """
            获取u_id
        :return: u_id
        """
        sql = "select id from user where username = %s"
        self.cursor.execute(sql, (self.__username,))
        data = self.cursor.fetchone()
        if data:
            return data[0]
        return -1

    def get_username(self) -> str:
        """
            获取用户名
        :return: 用户名
        """
        return self.__username
