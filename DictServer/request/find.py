"""

"""
from socket import socket

from request.abs_request import Request


class FindR(Request):

    def __init__(self, c_socket: socket, db, u_id: int):
        super().__init__(c_socket, db)
        self.__u_id = u_id

    def do_request(self, request):
        """
            查询单词结束
        :param request: "F word"
        """
        word = request[1]
        response = self.__get_definition(word)
        if response:
            self.__insert_history(self.__u_id, word)
            self.c_socket.send(response.encode())
        else:
            self.c_socket.send("查无此词".encode())

    def __insert_history(self, *args):
        """
            插入历史记录
        :param args: (u_id, word)
        """
        print(args)
        sql = "insert into history (u_id, record) values (%s, %s);"
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            print("插入成功")
        except Exception as e:
            print(e)
            self.db.rollback()
            print("插入失败")

    def __get_definition(self, *args) -> str:
        """
            查询数据库
        :return: 单词解释
        """
        sql = "select definition from dictionary where word = %s;"
        self.cursor.execute(sql, args)
        try:
            data = self.cursor.fetchone()[0]
            return data
        except Exception:
            return ""
