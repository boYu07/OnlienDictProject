"""
    请求接口
"""
from abc import abstractmethod


class Request:

    def __init__(self, database):
        self.__database = database
        self.__cursor = self.__database.cursor()

    @abstractmethod
    def do_request(self, field: str, table: str, data: str, request: str):
        pass
