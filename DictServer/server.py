"""
    服务端:
        目的可通过这个类快速的搭建起在线字典的服务端
"""
from socket import *
from typing import Optional

import pymysql

from request_thread import RequestThread


class DictServer:

    def __init__(self, *, host: str, port: int):
        self.__host = host
        self.__port = port

        self.__database = None  # type: Optional[pymysql]
        self.__s_socket = None  # type: Optional[socket]

        self.__init_socket()
        self.__socket_bind()

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if 0 <= value <= 65535:
            self.__port = value
        else:
            raise exit("超出0~66536范围")

    def __init_socket(self):
        """
            初始化tcp套接字并设置成监听套接字
        """
        self.__s_socket = socket()
        self.__s_socket.listen(10)

    def __socket_bind(self):
        """
            绑定服务器地址
        """
        address = (self.__host, self.__port)
        self.__s_socket.bind(address)

    def set_database(self, *, host: str, port=3306, user: str, password: str, database: str, charset="utf8"):
        """
            设置数据库
        :param host: 数据库地址
        :param port: 端口默认3306
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名
        :param charset: 编码
        """
        self.__database = pymysql.connect(host=host,
                                          port=port,
                                          user=user,
                                          password=password,
                                          database=database,
                                          charset=charset)

    def start(self):
        """
            启动服务
        """
        c_socket, c_address = self.__s_socket.accept()
        print(c_address, "已登录")
        request_thread = RequestThread(c_socket, self.__database)
        request_thread.setDaemon(True)
        request_thread.start()


# --------------------测试------------------------
if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 6489

    s = DictServer(host=HOST, port=PORT)
    s.start()
    s.set_database(host="localhost",
                   port=3306,
                   user="test",
                   password="123",
                   database="online_dict",
                   charset="utf8")
