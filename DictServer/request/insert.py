"""
    添加信息
"""
from request.request import Request


class Insert(Request):

    def __init__(self, database):
        super().__init__(database)

    def do_request(self, field: str, table: str, data: str, request: str):
        pass

