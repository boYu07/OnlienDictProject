"""

"""
from socket import socket

from controller.abs_controller import Controller


class FindC(Controller):

    def __init__(self, c_socket: socket):
        super().__init__(c_socket)

    def handle_request(self):
        """
            分情况组织请求
        """
        while True:
            word = input("查询: ")
            if not word:
                break
            request = "F " + word
            response = self.send_request(request)
            print(response)

    def send_request(self, request: str) -> str:
        """
            发送并接收反馈
        :param request: 请求
        :return: 反馈
        """
        self.c_socket.send(request.encode())
        response = self.c_socket.recv(1024)
        return response.decode()
