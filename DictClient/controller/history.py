"""

"""
from socket import socket

from controller.abs_controller import Controller


class HistoryC(Controller):
    def __init__(self, c_socket: socket):
        super().__init__(c_socket)

    def handle_request(self):
        """

        :return:
        """
        request = "H"
        response = self.send_request(request)
        print(response)

    def send_request(self, request: str) -> str:
        """
            发送请求
        :param request: 请求
        :return: 反馈
        """
        self.c_socket.send(request.encode())
        return self.c_socket.recv(2048).decode()
