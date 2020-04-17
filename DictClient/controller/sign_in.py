"""
    登录
"""
from socket import socket

from controller.abs_controller import Controller


class SignInC(Controller):

    def __init__(self, c_socket: socket):
        super().__init__(c_socket)
        self.__username = ""

    def handle_request(self) -> int:
        """
            分情况组织请求
        :return: 0: 退出, 1: 失败, 2: 成功
        """
        username = input("输入用户名: ")
        if username == "quit":
            return 0
        request = "L U " + username
        response = self.send_request(request)
        if response == "N":
            return 1
        self.__username = username

        password = input("输入密码: ")
        if password == "quit":
            return 0
        request = "L P " + password
        response = self.send_request(request)
        if response == "N":
            return 1
        return 2

    def send_request(self, request: str) -> str:
        """
            发送并接收反馈
        :param request: 请求
        :return: 收到回馈
        """
        self.c_socket.send(request.encode())
        response = self.c_socket.recv(128)
        return response.decode()

    def get_username(self) -> str:
        """
            获取用户名
        :return: 用户名
        """
        return self.__username
