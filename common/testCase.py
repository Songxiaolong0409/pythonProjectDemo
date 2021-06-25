"""
测试用例实例
"""
from enum import Enum


class TestCaseEnum(Enum):
    NAME = "name",
    CASE = "case"


class TestCase(object):

    __attr__ = [
        TestCaseEnum.NAME,
        TestCaseEnum.CASE
    ]

    def __init__(self, name, case=[]):
        self.name = name
        self.case = case
