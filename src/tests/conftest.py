from time import strftime

import pytest
from py.xml import html

from src.main.common.excelUtil import get_excel_test_case
from src.tests import test_case


def pytest_addoption(parser):
    """
    自定义命令行参数
    --e 切换环境参数 dev、test、pre、prd  default test
    """
    parser.addoption("--e", action="store", default="test")


@pytest.fixture(scope="session")
def option_e(request):
    return request.config.getoption("--e")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例描述'))
    # 删除原第三列表头
    cells.pop(2)
    cells.insert(2, html.th('用例'))
    cells.insert(3, html.th('操作时间', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()
    cells.pop(-1)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    # 删除原第三列数据
    cells.pop(2)
    cells.insert(2, html.td(report.nodeid))
    cells.insert(3, html.td(strftime('%Y-%m-%d %H:%M:%S'), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))
    cells.pop()
    cells.pop(-1)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文
    if report.when == "call":
        # always add url to report
        # extra.append(pytest_html.extras.url("http://www.example.com/"))
        # xfail = hasattr(report, "wasxfail")
        # if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extra.append(pytest_html.extras.html("<div class='empty log'>" + report.longreprtext + "<br/></div>"))
            # extra.append(pytest_html.extras.html("<div class='empty log'>" + report.caplog + "<br/></div>"))
            # extra.append(pytest_html.extras.html("<div class='empty log'>"+report.capstderr+"<br/></div>"))
            # extra.append(pytest_html.extras.json(extra))
        report.extra = extra


def pytest_html_results_table_html(report, data):
    del data[:]
    if report.failed:
        data.append(html.div(report.caplog, class_='empty log'))
        data.append(html.div(report.longreprtext, class_='empty log'))
    else:
        data.append(html.div(report.sections.__getitem__(report.sections.__len__()-1), class_='empty log'))


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "接口测试报告"


# 修改Environment部分信息，配置测试报告环境信息
def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["Auth"] = "xiaolong.song"
    config._metadata['Email'] = 'xiaolong.song@fih-foxconn.com'
    config._metadata['开始时间'] = strftime('%Y-%m-%d %H:%M:%S')
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Platform")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")


# 修改Summary部分的信息
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("所属部门: 技术部")])
#     prefix.extend([html.p("测试人: 大帅哥")])


def pytest_collection_modifyitems(session, items):
    """
    session 下的items 可改变pytest执行的测试用例
    items 改变执行顺序
    """
    test_case_file = session.config.args[0][:-7]+"_test_case.xlsx"
    # 从excel里读取测试用例放入全局
    excel_test_case = get_excel_test_case(test_case_file)

    # 设置pytest执行的test用例函数和顺序
    excel_items = []
    for case in excel_test_case:
        excel_items.append("test_"+case.name)
        test_case.__setitem__(case.name, case.case)

    # 将用例名拿出来存入新列表
    new_items = []
    for excel_item in excel_items:
        for item in items:
            if excel_item == item.name:
                new_items.append(item)

    items = new_items
    session.items = new_items
