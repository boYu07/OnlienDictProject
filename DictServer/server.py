"""
    服务端:
        目的可通过这个类快速的搭建起在线字典的服务端
"""
from socket import *
from typing import Optional


class DictServer:

    def __init__(self, *, host: str, port: int, database: str):
        self.__host = host
        self.__port = port
        self.__database = database

        self.__s_socket = None  # type: Optional[socket]
        self.__init_socket()
        self.__socket_bind()

    def start(self):
        """
            启动服务
        """
        self.__s_socket.accept()

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


# --------------------测试------------------------
if __name__ == '__main__':
    HOST = "0.0.0.0"
    PORT = 6489
    DATABASE = ""

    s = DictServer(host=HOST, port=PORT, database=DATABASE)
    s.start()
