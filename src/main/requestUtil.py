import requests

from src.main.common.logging import log
from src.main.common import __is_json_array, __is_json
from src.main.environment import Environment


def http(method, url, token, data):
    headers = {"Authorization": "Bearer {}".format(token)}
    if token != "" and token is not None:
        if __is_json_array(data) or __is_json(data):
            return requests.request(method, url, json=data, headers=headers)
        else:
            return requests.request(method, url, data=data, headers=headers)

    return requests.request(method, url, data=data)


def get(url, token, data):
    return http("get", url, token, data)


def post(url, token, data):
    return http("post", url, token, data)


class HttpApi(object):

    __attr__ = [
        "param_data",
        "token",
        "environment",
        "req_action",
        "url"
    ]

    def __init__(self, param_data, token, environment, req_action, impl_obj=Environment):
        self.param_data = param_data
        self.token = token
        self.environment = environment
        self.req_action = req_action
        self.url = Environment.get_environment(impl_obj, environment).url + self.req_action

    def post(self):
        log.info("请求地址:%s", self.url)
        log.info("request:%s", self.param_data)
        response = post(self.url, self.token, self.param_data)
        log.info("response:%s", response.text)
        return response

    def get(self):
        log.info("请求地址:%s", self.url)
        log.info("request:%s", self.param_data)
        response = get(self.url, self.token, self.param_data)
        log.info("response:%s", response.text)
        return response
