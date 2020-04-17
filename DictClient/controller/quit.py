"""

"""
from socket import socket

from controller.abs_controller import Controller


class QuitC(Controller):

    def __init__(self, c_socket: socket):
        super().__init__(c_socket)

    def handle_request(self) -> int:
        """
            分情况组织请求
        :return: 0: 退出, 1: 失败, 2: 成功
        """
        request = "Q"
        self.send_request(request)
        return 2

    def send_request(self, request: str) -> str:
        """
            发送请求
        :param request:
        :return:
        """
        self.c_socket.send(request.encode())
        return ""
