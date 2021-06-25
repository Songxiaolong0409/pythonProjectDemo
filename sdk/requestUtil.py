import requests


def http(method, url, token, data):
    headers = {"Authorization", "Bearer {}".format(token)}
    if token != "" and token is not None:
        return requests.request(method, url, data=data, headers=headers)

    return requests.request(method, url, data=data)


def get(url, token, data):
    return http("get", url, token, data)


def post(url, token, data):
    return http("post", url, token, data)
