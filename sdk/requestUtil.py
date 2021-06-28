import requests

from common.testCaseAnalysis import __is_json_array, __is_json


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
