import json
from enum import Enum

from sdk.ics import Environment, AREA_CODE


class ResultEnum(Enum):
    CODE = "code"
    SUCCESS = "success"
    MESSAGE = "message"
    DATA = "data"


class ParamEnum(Enum):
    URL = "url"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    GRANT_TYPE = "grant_type"
    USER_TYPE = "userType"
    AREA_CODE = "areaCode"
    MOBILE = "mobile"
    USERNAME = "username"
    PASSWORD = "password"


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


class Param(object):

    __attr__ = [
        ParamEnum.URL,
        ParamEnum.CLIENT_ID,
        ParamEnum.CLIENT_SECRET,
        ParamEnum.GRANT_TYPE,
        ParamEnum.USER_TYPE,
        ParamEnum.AREA_CODE,
        ParamEnum.MOBILE,
        ParamEnum.USERNAME,
        ParamEnum.PASSWORD,
    ]

    def __init__(self, grant_type, area_code, mobile, username, password,
                 environment):
        t = Environment.get_ics_environment(environment)

        if area_code == AREA_CODE:
            area_code = "%2B86"

        self.url = t.url
        self.client_id = t.client_id
        self.client_secret = t.client_secret
        self.userType = t.usertype
        self.grant_type = grant_type
        self.areaCode = area_code
        self.mobile = mobile
        self.username = username
        self.password = password


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
