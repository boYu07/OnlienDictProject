"""
    注册
"""
from socket import socket
from typing import List

from request.abs_request import Request


class SignOnR(Request):

    def __init__(self, c_socket: socket, db):
        super().__init__(c_socket, db)
        self.__username = ""

    def do_request(self, request: List[str]):
        """
            处理请求
        :param request: ["R", "username password"]
        """
        username, password = request[1].split(" ")
        # 插入请求
        response = self.__register_user(username, password)
        if not response:
            self.c_socket.send(b"N")
            return
        self.c_socket.send(b"Y")
        self.__username = username

    def __register_user(self, *args) -> bool:
        """
            插入用户数据
        :param args: (username, password)
        :return: 成功 True, 失败 False
        """
        print(args)
        # sql = "insert into user (username, password) value (zby,123);"
        sql = "insert into user (username, password) value (%s,%s);"
        print(sql)
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def get_username(self):
        return self.__username

    def get_u_id(self) -> int:
        """
            获取u_id
        :return: u_id
        """
        sql = "select id from user where username = %s"
        self.cursor.execute(sql, (self.__username,))
        return self.cursor.fetchone()[0]
