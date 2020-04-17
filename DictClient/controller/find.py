"""

"""
from socket import socket

from controller.abs_controller import Controller


class FindC(Controller):

    def __init__(self, c_socket: socket, username):
        super().__init__(c_socket)
        self.__username = username

    def handle_request(self) -> int:
        """
            分情况组织请求
        :return: 0: 退出, 1: 失败, 2: 成功
        """
        cmd = input(">>")
        if cmd == "sign out":
            return 0
        if "find" in cmd:
            request = "F W " + cmd
            response = self.send_request(request)
            if response == "N":
                return 1
            if response == "Y":
                return 2
        if cmd == "history":
            request = "F H " + self.__username
            response = self.send_request(request)
            if response == "N":
                return 1
            if response == "Y":
                return 2
        print(cmd, "无效命令")

    def send_request(self, request: str) -> str:
        """
            发送并接收反馈
        :param request: 请求
        :return: 收到回馈
        """
        self.c_socket.send(request.encode())
        response = self.c_socket.recv(128)
        return response.decode()

    def get_content(self) -> str:
        """
            获取具体内容
        :return: 返回具体的查询内容
        """
        data = self.c_socket.recv(1024)
        return data.decode()
