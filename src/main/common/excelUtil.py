"""
Excel操作工具
主要是用来获取excel里的测试用例数据
"""
import sys

import xlrd as xlrd

from src.main.common.testCase import TestCase
from src.main.common.logging import log


def get_file(filename):
    """新版xlrd报 Excel xlsx file； not supported
    解决办法：安装旧版本 pip install xlrd == 1.2.0"""
    #  拼接读取文件的绝对路径

    # case_path = os.path.join(os.path.dirname(__file__), r'../'+filename)
    case_path = sys.path[3] + "/"+filename
    #  读取文件
    book = xlrd.open_workbook(case_path)
    return book


def get_sheet(workbook, sheet_name):
    #  指定读取文件中的页名
    sheet = workbook.sheet_by_name(sheet_name)
    return sheet


def get_excel_test_case(filename):
    """
    读取Excel文件
    获取 文件中的测试用例信息
    """
    excel_test_case = []

    try:
        workbook = get_file(filename)
        sheet = workbook.sheet_by_index(0)

        for row in range(sheet.nrows):
            name = ""
            case = []

            if row == 0:
                continue
            for cel in range(sheet.ncols):
                if cel == 0:
                    name = sheet.cell_value(row, cel)
                else:
                    val = sheet.cell_value(row, cel)
                    if val != "":
                        case.append(val)
            test_case = TestCase(name, case)
            excel_test_case.append(test_case)
    except BaseException as e:
        log.info("获取Excel 数据错误", e.__dict__)

    return excel_test_case

