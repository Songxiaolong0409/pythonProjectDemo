from sdk.ics import entity
from sdk.ics.entity import User


def get_response(response):
    try:
        res = entity.Result(response.text)
        if res.code == 200:
            return User(res.data)
        elif res.code == 500:
            return res.message
    except Exception as e:
        return "请求异常:" + e


def pytest_assert(response):
    try:
        res = entity.Result(response.text)
        assert res.code != 200, res.message
    except Exception as e:
        assert False, e.args
