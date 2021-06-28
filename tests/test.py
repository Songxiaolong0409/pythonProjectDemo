import json
import sys

import pytest

from common.testCaseAnalysis import test_case_analysis
from sdk.ics.entity import Result
from sdk.ics.ics import login_username_pwd
from common.logging import log
from tests import api_result


@pytest.fixture(scope="session")
def ics_login(option_e):
    result = login_username_pwd(option_e, "admin", "Fih123456")

    if isinstance(result, str):
        assert False, result
    else:
        return result


def test_method1(option_e, ics_login):
    """
    html测试报告test1 说明
    :param ics_login:
    :return:
    """
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]

    data = {}
    data.__setitem__("access_token", ics_login.access_token)

    d = {}
    t = {}
    t.__setitem__("abc", data)
    d.__setitem__("code", 200)
    d.__setitem__("data", t)
    d.__setitem__("success", None)
    d.__setitem__("message", None)

    res = Result(json.dumps(d))

    api_result.__setitem__(param_key, res)
    assert ics_login.access_token != "", "测试登录失败了"


def test_method2(option_e, ics_login):
    method_name = sys._getframe().f_code.co_name
    param_key = method_name[5:]
    case = test_case_analysis(api_result, param_key)
    log.info("test2============="+str(case))
    t = "tt"
    assert t == "tt", "test2 异常了"


def test_method3():
    log.info("test3=============")
    # p2 = test_method2()
    # assert p2, "test3 p2=true"
    # assert p2 is False, "test3 p2=false"


# pytest -s test.py --e test --html ../report/report.html
# -k "test1 or test2" 只执行设定的方法
if __name__ == "__main__":
    pytest.main(["test.py",
                 "-s",
                 "--e=pre",
                 "--html=../report/report.html",
                 "--self-contained-html"])
