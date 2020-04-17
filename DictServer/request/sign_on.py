"""
    注册
"""
from socket import socket

from request.abs_request import Request


class SignOnR(Request):

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
        response = self.insert(username, password)
        if not response:
            self.c_socket.send(b"N")
            return
        self.c_socket.send(b"Y")

    def insert(self, *args):
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
