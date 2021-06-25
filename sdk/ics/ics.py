import requests

from sdk import get_response
from sdk.ics import AREA_CODE, entity
from common.logging import log


def __login(environment, grant_type, area_code, mobile, username, password):
    form_data = entity.Param(grant_type, area_code, mobile, username, password, environment)
    result = get_response(requests.post(form_data.url+"/oauth/token", form_data.__dict__))
    log.info("login request:%s", form_data.__dict__)
    log.info("login response:%s", isinstance(result, str) and result or result.__dict__)
    return result


def login_password(environment, mobile, area_code=AREA_CODE):
    # 手机号密码方式获取token，api4
    result = __login(environment, "pwd", area_code, mobile, None, None)
    return result


def login_username_pwd(environment, username, password):
    # 用户名密码方式登录
    return __login(environment, "password", None, None, username, password)
