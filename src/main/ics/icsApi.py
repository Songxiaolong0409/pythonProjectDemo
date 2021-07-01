import requests

from src.main import get_response
from src.main.environment import Environment
from src.main.common.logging import log
from src.main.ics import ICS


def login(impl_obj=Environment, environment=str):
    form_data = Environment.get_environment(impl_obj, environment)
    url = Environment.get_environment(ICS(), environment).url
    form_data.__setattr__("url", url)

    result = get_response(requests.post(url+"/oauth/token", form_data.__dict__))
    log.info("login request:%s", form_data.__dict__)
    log.info("login response:%s", isinstance(result, str) and result or result.__dict__)

    return result
