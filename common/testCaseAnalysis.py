"""
excel里的testcase，如果含有变量，则把变量替换成参数
"""
import json
import sys

from common.logging import log
from tests.conftest import test_case


def test_case_analysis(api_result=dict, param_key=dict):
    """
    解析Excel里的case的变量
    :param param_key: 存放在全局变量里的参数，用来替换test_case里的spel表达式
    :return:
    """
    try:
        case_list = test_case.get(param_key)
        log.info("执行方法：%s，参数：%s", param_key, case_list)
        for case in case_list:
            # 如果测试用例是数组，则遍历，且基本证明为jsonArray
            if __is_json_array(case):
                array = json.loads(case)
                for json_case in array:
                    __test_case_analysis_recursion(api_result, json_case)

                log.info("方法：%s，最终Json参数：%s", param_key, str(array))
                return array
            # 如果case用例为json类型
            elif __is_json(case):
                json_case = json.loads(case)
                __test_case_analysis_recursion(api_result, json_case)

                log.info("方法：%s，最终Json参数：%s", param_key, str(json_case))
                return json_case
            # 如果case用例为字符串类型，则可能为get请求参数
            elif __is_args(case):
                args = ""
                params = str(case).split("&")
                for param in params:
                    val = param.split("=")[1]
                    args.join(param.split("=")[0])
                    args.join("&").join(__get_test_case_val(api_result, val))

                log.info("方法：%s，最终String参数：%s", param_key, args)
                return args
            else:
                error_msg = "暂不支持的参数类型，或参数类型错误%s"
                log.error(error_msg, case)
                raise Exception(error_msg)
    except BaseException as e:
        log.error(e.args)
        sys.exit()


def __test_case_analysis_recursion(api_result=dict, json_case=dict):
    """
    递归 解析测试用例里的表达式，并给表达式赋值
    :param json_case: 测试用例
    :return:
    """
    for key in json_case:
        if isinstance(json_case[key], dict):
            __test_case_analysis_recursion(api_result, json_case[key])
        else:
            val = json_case[key]
            json_case[key] = __get_test_case_val(api_result, val)


def __get_test_case_val(api_result=dict, spel_str_key=str):
    """
    根据测试用例表达式，获取对应的参数值
    :param spel_str_key: 测试用例表达式
    :return:
    """
    if __is_spel_str(spel_str_key):
        spel_key = __get_spel_key(spel_str_key).split(".")
        result = api_result[spel_key[0]]
        if result.code == 200:
            return __get_test_case_val_recursion(result.data, spel_key)
    return spel_str_key


def __get_test_case_val_recursion(data=dict, spel_key=dict, i=1):
    """
    递归 根据测试用例表达式，获取对应的参数值
    :param data: 参数值对象
    :param spel_key: 表达式集合
    :param i: 表达式下标
    :return:
    """
    if isinstance(data, list):
        spel_val = data.__getitem__(0)[spel_key[i]]
    else:
        spel_val = data.get(spel_key[i])
    if isinstance(spel_val, dict):
        return __get_test_case_val_recursion(spel_val, spel_key, i+1)
    elif isinstance(spel_val, list):
        return __get_test_case_val_recursion(spel_val.__getitem__(0), spel_key, i+1)
    else:
        return spel_val


def __is_spel_str(string=str):
    """
    判断字符串是否是spel格式
    :param string:  字符串
    :return:
    """
    if isinstance(string, bool):
        return False
    elif isinstance(string, str) and string.startswith("${") and string.endswith("}"):
        return True
    else:
        return False


def __get_spel_key(string=str):
    """
    获取spel表达式里的key字串
    :param string: 包含spel的字符串
    :return:
    """
    return string[2:-1]


def __is_json_array(json_str):
    if isinstance(json_str, str):
        if json_str.startswith("[") and json_str.endswith("]"):
            return True
    if isinstance(json_str, list):
        return True


def __is_json(json_str):
    if isinstance(json_str, dict):
        return True
    else:
        try:
            json.loads(json_str)
            return True
        except:
            return False


def __is_args(string=str):
    if __is_json(string) is False:
        if isinstance(string, str):
            if "&" in string:
                return True
    return False
