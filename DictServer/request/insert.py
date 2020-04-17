"""
    添加信息
"""
from typing import List


class Insert:

    def __init__(self, cursor, db):
        self.__db = db
        self.__cursor = cursor

    def insert(self, data: List[str], table="", field=""):
        print(data)
        # sql = "insert into user (username, password) value (request);"
        sql = "insert into %s (%s) value " % (table, field)
        sql += "(%s);"
        print(sql)
        try:
            self.__cursor.execute(sql, data)
            self.__db.commit()
            return True
        except Exception:
            self.__db.rollback()
            return False
