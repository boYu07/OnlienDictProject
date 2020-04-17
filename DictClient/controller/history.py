"""

"""
from socket import socket

from controller.abs_controller import Controller


class HistoryC(Controller):
    def __init__(self, c_socket: socket, username):
        super().__init__(c_socket)
        self.__username = username

    def handle_request(self):
        """

        :return:
        """
        request = "H " + self.__username
        response = self.send_request(request)
        print(response)

    def send_request(self, request: str) -> str:
        """

        :param request:
        :return:
        """
        self.c_socket.send(request.encode())
        return self.c_socket.recv(2048).decode()
