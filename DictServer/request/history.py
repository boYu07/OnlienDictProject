"""

"""
from socket import socket

from request.abs_request import Request


class HistoryR(Request):

    def __init__(self, c_socket: socket, db, u_id: int):
        super().__init__(c_socket, db)
        self.__u_id = u_id

    def do_request(self, request=""):
        """
            查询历史
        :param request: ""
        """
        response = self.__get_history()
        if response:
            self.c_socket.send(response.encode())
        else:
            self.c_socket.send("无记录".encode())

    def __get_history(self) -> str:
        """
            获取历史记录
        :return: 记录信息
        """
        sql = "select time, username, " \
              "record from history as h left join user as u " \
              "on h.u_id = u.id where u.id = %s " \
              "order by time desc " \
              "limit 10;"

        self.cursor.execute(sql, (self.__u_id,))
        response = ""
        for item in self.cursor.fetchall():
            response += "%s\t%s\t%s\n" % item
        return response
