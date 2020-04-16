"""

"""
import sys
from typing import Tuple


class DictController:

    def __init__(self):
        pass

    def handle_request(self, data: str) -> Tuple[bool, str]:
        if data == "Q":
            sys.exit("程序退出")
        return (True, "收到%s" % data)  # 测试
