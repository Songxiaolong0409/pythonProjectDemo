from sdk.ics import entity
from sdk.ics.entity import User
from tests import api_result


def get_response(response):
    try:
        res = entity.Result(response.text)
        if res.code == 200:
            return User(res.data)
        elif res.code == 500:
            return res.message
    except Exception as e:
        return "请求异常:" + e


def pytest_assert(response, param_key):
    try:
        if response.status_code == 200:
            res = entity.Result(response.text)
            api_result.__setitem__(param_key, res)
            assert res.code == 200, res.message
        else:
            assert False, response.text
    except Exception as e:
        assert False, e.args
