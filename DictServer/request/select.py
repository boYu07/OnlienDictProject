"""
    从数据库查询
"""
from request.request import Request


class Select(Request):

    def __init__(self, database):
        super().__init__(database)

    def do_request(self, field: str, table: str, data: str, request: str):
        sql = "select %s from %s where %s = " % (field, table, data)
        sql += "%s;"
        self.__cursor.execute(sql, [request])
        value = self.__cursor.fetchone()
        if not value:
            return "N 没有找到"
        return "Y " + value
