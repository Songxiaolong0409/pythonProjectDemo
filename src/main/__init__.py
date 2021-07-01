import json
from enum import Enum

from src.tests import api_result


def get_response(response):
    try:
        res = Result(response.text)
        if res.code == 200:
            return User(res.data)
        elif res.code == 500:
            return res.message
    except Exception as e:
        return "请求异常:" + e


def pytest_assert(response, param_key):
    try:
        if response.status_code == 200:
            res = Result(response.text)
            api_result.__setitem__(param_key, res)
            assert res.code == 200, res.message
        else:
            assert False, response.text
    except Exception as e:
        assert False, e.args


class ResultEnum(Enum):
    CODE = "code"
    SUCCESS = "success"
    MESSAGE = "message"
    DATA = "data"


class UserEnum(Enum):
    USER_ID = "userId"
    CLIENT_ID = "clientId"
    AREA_CODE = "areaCode"
    MOBILE = "mobile"
    USERNAME = "username"
    USER_NAME = "user_name"
    EMAIL = "email"
    STATUS = "status"
    ACCESS_TOKEN = "access_token"


class Result(object):

    __attr__ = [
        ResultEnum.CODE, ResultEnum.SUCCESS, ResultEnum.MESSAGE, ResultEnum.DATA
    ]

    def __init__(self, string):
        response = json.loads(string)
        self.code = response.get(ResultEnum.CODE.value)
        self.success = response.get(ResultEnum.SUCCESS.value)
        self.message = response.get(ResultEnum.MESSAGE.value)
        self.data = response.get(ResultEnum.DATA.value)


class User(object):
    __attr__ = [
        UserEnum.USER_ID,
        UserEnum.CLIENT_ID,
        UserEnum.AREA_CODE,
        UserEnum.MOBILE,
        UserEnum.USERNAME,
        UserEnum.USER_NAME,
        UserEnum.EMAIL,
        UserEnum.STATUS,
        UserEnum.ACCESS_TOKEN
    ]

    def __init__(self, string):
        userinfo = string[UserEnum.USER_NAME.value]
        self.access_token = string.get(UserEnum.ACCESS_TOKEN.value)
        self.user_id = userinfo.get(UserEnum.USER_ID.value)
        self.client_id = userinfo.get(UserEnum.CLIENT_ID.value)
        self.status = userinfo.get(UserEnum.STATUS.value)
        self.areaCode = userinfo.get(UserEnum.AREA_CODE.value)
        self.mobile = userinfo.get(UserEnum.MOBILE.value)
        self.username = userinfo.get(UserEnum.USERNAME.value)
        self.email = userinfo.get(UserEnum.EMAIL.value)
