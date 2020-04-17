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
                成功:进入二级界面
                失败:重新输入/返回一级界面/退出
        注册界面:
            1. 输入用户名
            2. 输入密码
                成功:进入二级界面
                失败:重新输入/返回一级界面/退出
"""
import sys
from socket import *
from typing import Optional

from controller.find import FindC
from controller.history import HistoryC
from controller.quit import QuitC
from controller.sign_in import SignInC
from controller.sign_on import SignOnC


class DictClient:

    def __init__(self):
        self.__controller = None
        self.__username = ""
        self.__c_socket = None  # type: Optional[socket]

    def __main_menu(self):
        """
            一级界面
                1. 登录
                    进入登录界面
                2. 注册
                    进入注册界面
                3. 退出
        """
        self.__username = ""
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
        """
            一级界面命令帮助
        """
        print("+---------------+---------------+")
        print("|   命令\t|   命令提示\t|")
        print("+---------------+---------------+")
        print("|   sign in\t|   登录\t|")
        print("|   sign on\t|   注册用户\t|")
        print("|   quit\t|   退出程序\t|")
        print("+---------------+---------------+")

    def __sign_in_menu(self):
        """
            登录界面
        """
        print("===============登录==============")
        self.__controller = SignInC(self.__c_socket)
        while True:
            response = self.__controller.handle_request()
            if not response:
                return self.__main_menu()
            if response == 1:
                print("登录失败")
                continue
            if response == 2:
                print("登录成功")
                self.__username = self.__controller.get_username()
                return self.__sub_menu()

    def __sign_on_menu(self):
        """
            注册界面
        """
        print("===============注册==============")
        self.__controller = SignOnC(self.__c_socket)
        while True:
            response = self.__controller.handle_request()
            if not response:
                return self.__main_menu()
            if response == 1:
                print("注册失败")
                continue
            if response == 2:
                print("注册成功")
                return self.__sub_menu()

    def __sub_menu(self):
        """
            二级界面
                1. 查询单词
                    调用查询功能,
                2. 历史记录
                    调用历史记录功能
                3. 注销
                    返回一级界面
        """
        print("===============查询==============")
        self.__request_command()
        while True:
            cmd = input(">>")
            if cmd == "sign out":
                return self.__main_menu()
            if cmd == "find":
                self.__controller = FindC(self.__c_socket, self.__username)
                self.__controller.handle_request()
            if cmd == "history":
                self.__controller = HistoryC(self.__c_socket, self.__username)
                self.__controller.handle_request()

    @staticmethod
    def __request_command():
        """
            二级界面命令帮助
        """
        title_cmd = "命令"
        title_help = "命令提示"
        cmd_find = "find"
        cmd_history = "history"
        cmd_sign_out = "sign out"
        help_find = "进入查询单词"
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
        """
            退出程序
        """
        self.__controller = QuitC(self.__c_socket)
        response = self.__controller.handle_request()
        if response == 2:
            sys.exit("客户端退出")

    def connect(self, address):
        """
            建立连接
        :param address: 服务器地址
        """
        self.__c_socket = socket()
        self.__c_socket.connect(address)

    def main(self):
        """
            启动服务
        """
        try:
            self.__main_menu()
        except KeyboardInterrupt:
            return self.__quit()


if __name__ == '__main__':
    ADDRESS = ("localhost", 6489)

    v = DictClient()

    v.connect(ADDRESS)
    v.main()
