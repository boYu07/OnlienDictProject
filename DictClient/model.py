"""
    用户数据model
"""


class UserInfoModel:

    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
