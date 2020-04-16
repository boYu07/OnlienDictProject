"""
    客户端界面
        一级界面:
            1. 登录
                进入登录界面
            2. 注册
                进入注册界面
            3. 退出
        二级界面:
            1. 查询单词
                调用查询功能,
            2. 历史记录
                调用历史记录功能
            3. 注销
                返回一级界面
        登录界面:
            1. 输入用户名
            2. 输入密码
                调用登录功能
                    成功:进入二级界面
                    失败:重新输入/返回一级界面/退出
        注册界面:
            1. 填写用户名
                调用设置用户名功能
            2. 填写密码
                二段密码校验
                调用密码设置功能
            3. 注册成功进入二级界面
            4. 随时可以退出
"""
from typing import Optional

from bll import RequestController


class DictClient:

    def __init__(self):
        self.__controller = None  # type: Optional[RequestController]
        self.__username = ""

    def __main_menu(self):
        while True:
            print("===============欢迎==============")
            self.__main_help()
            cmd = input(">>")
            if cmd == "sign in":
                return self.__sign_in_menu()
            if cmd == "sign on":
                return self.__sign_on_menu()
            if cmd == "quit":
                return self.__quit()
            print(cmd, "无效命令")

    @staticmethod
    def __main_help():
        print("+---------------+---------------+")
        print("|   命令\t|   命令提示\t|")
        print("+---------------+---------------+")
        print("|   sign in\t|   登录\t|")
        print("|   sign on\t|   注册用户\t|")
        print("|   quit\t|   退出程序\t|")
        print("+---------------+---------------+")

    def __sign_in_menu(self):
        print("===============登录==============")
        while True:
            username = input("输入用户名: ")
            if username == "quit":
                return self.__main_menu()
            request = "L U " + username
            response = self.__controller.handle_request(request)
            if not response[0]:
                print(response[1])
                continue
            password = input("输入密码: ")
            if password == "quit":
                return self.__main_menu()
            request = "L P " + password
            response = self.__controller.handle_request(request)
            if not response[0]:
                print(response[1])
                continue
            print("登录成功!")
            self.__username = username
            return self.__sub_menu()

    def __sign_on_menu(self):
        print("===============注册==============")
        while True:
            username = input("输入用户名: ")
            if username == "quit":
                return self.__main_menu()
            request = "R U " + username
            response = self.__controller.handle_request(request)
            if not response[0]:
                print(response[1])
                continue
            password = input("输入密码: ")
            if password == "quit":
                return self.__main_menu()
            request = "R P " + password
            response = self.__controller.handle_request(request)
            print(response[1])
            self.__username = username
            return self.__sub_menu()

    def __sub_menu(self):
        print("===============查询==============")
        while True:
            self.__request_command()
            cmd = input(">>")
            if cmd == "sign out":
                return self.__main_menu()
            if "find" in cmd:
                request = "F W " + cmd
                response = self.__controller.handle_request(request)
                print(response[1])
                continue
            if cmd == "history":
                request = "F H " + self.__username
                response = self.__controller.handle_request(request)
                print(response[1])
                continue
            print(cmd, "无效命令")

    @staticmethod
    def __request_command():
        title_cmd = "命令"
        title_help = "命令提示"
        cmd_find = "find 单词"
        cmd_history = "history"
        cmd_sign_out = "sign out"
        help_find = "查询单词解释"
        help_history = "查看查询历史"
        help_sign_out = "返回最初界面"
        print("+---------------+-----------------------+")
        print("|   " + title_cmd + "\t|   " + title_help + "\t\t|")
        print("+---------------+-----------------------+")
        print("|   " + cmd_find + "\t|   " + help_find + "\t|")
        print("|   " + cmd_history + "\t|   " + help_history + "\t|")
        print("|   " + cmd_sign_out + "\t|   " + help_sign_out + "\t|")
        print("+---------------+-----------------------+")

    def __quit(self):
        self.__controller.handle_request("Q")

    def connect(self, address):
        self.__controller = RequestController(address)

    def main(self):
        try:
            self.__main_menu()
        except KeyboardInterrupt:
            return self.__quit()


if __name__ == '__main__':
    ADDRESS = ("localhost", 6489)

    v = DictClient()
    v.main()
    v.connect(ADDRESS)
