"""

"""
from socket import socket

from request.abs_request import Request


class SignInR(Request):

    def __init__(self, c_socket: socket, db):
        super().__init__(c_socket, db)

    def do_request(self, request):
        """

        :param request:
        :return:
        """
        username = request[1]
        password = request[2]
        # 插入请求
        response = self.select(username, password)
        if not response:
            self.c_socket.send(b"N")
            return
        self.c_socket.send(b"Y")

    def select(self, *args) -> bool:
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
