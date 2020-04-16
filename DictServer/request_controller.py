"""
    服务端 请求解析
"""
from request.select import Select


class RequestController:

    def __init__(self, database):
        self.__database = database
        self.__cursor = self.__database

    def handle_request(self, request: bytes):
        """
            解析请求请求
        :param request: 请求信息
        """
        while True:
            list_data = request.decode().split(" ", 2)
            print(list_data)  # debug
            request_type = list_data[0]
            if request_type == "L":
                # 登录请求
                if list_data[1] == "U":
                    # 查询请求
                    Select(self.__database).do_request("username", "user", "username", list_data[2])
                if list_data[1] == "P":
                    # 密码请求
                    pass
                continue
            if request_type == "R":
                # 注册请求
                if list_data[1] == "U":
                    # 查询请求
                    pass
                if list_data[1] == "P":
                    # 密码请求
                    pass
                continue
            if request_type == "F":
                # 查询请求
                if list_data[1] == "W":
                    # 解释请求
                    pass
                    continue
                if list_data[1] == "H":
                    # 历史请求
                    pass
                continue
            if request_type == "Q":
                return
            print("未知请求")
