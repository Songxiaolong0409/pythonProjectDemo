from abc import ABCMeta, abstractmethod
from enum import Enum

from src.main.profilesActive import ProfilesActiveEnum


class Active(Enum):
    URL = "url"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    USER_TYPE = "userType"
    GRANT_TYPE = "grant_type"
    AREA_CODE = "areaCode"
    MOBILE = "mobile"
    USERNAME = "username"
    PASSWORD = "password"


class Environment(object):

    __metaclass__ = ABCMeta  # 这是一个抽象类

    __attr__ = [
        Active.URL,
        Active.CLIENT_ID,
        Active.CLIENT_SECRET,
        Active.USER_TYPE,
        Active.GRANT_TYPE,
        Active.AREA_CODE,
        Active.MOBILE,
        Active.USERNAME,
        Active.PASSWORD,
    ]

    def __init__(self, url, client_id, client_secret, usertype, grant_type,
                 area_code, mobile, username, password):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.usertype = usertype
        self.areaCode = area_code
        self.mobile = mobile
        self.username = username
        self.password = password

    def get_environment(self, environment):
        if environment == ProfilesActiveEnum.DEV.value:
            return self.dev()
        elif environment == ProfilesActiveEnum.TEST.value:
            return self.test()
        elif environment == ProfilesActiveEnum.PRE.value:
            return self.pre()
        elif environment == ProfilesActiveEnum.PRD.value:
            return self.prd()
        elif environment == ProfilesActiveEnum.AWS.value:
            return self.aws()
        else:
            return self.test()

    @abstractmethod
    def dev(self):
        pass

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def pre(self):
        pass

    @abstractmethod
    def prd(self):
        pass

    @abstractmethod
    def aws(self):
        pass
