# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-06 下午 14:05
@project : api_frame
@Author  : xhb
@Site    : 
@File    : login.py
@Software: PyCharm Community Edition
"""

from common.http_request import HttpRequest
import unittest
from common.read_conf import *
from common.do_excel import DoExcel
from ddt import ddt, data
from common.logger import Mylog

test_date = DoExcel(sheet_file, sheet_name).get_data()


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.t = DoExcel(sheet_file, sheet_name)
        self.logger = Mylog("root")

    @data(*test_date)
    def test_login(self, item):
        self.logger.info("******************************")
        self.logger.info("正在执行的用例是 {}".format(item["title"]))
        self.logger.info("请求的数据是：{0}".format(item["data"]))
        res = HttpRequest().http_request(item["url"], eval(item["data"]), item["method"], item["type"])
        try:
            self.assertEqual(item["ExpectResult"], res.json()["message"])
            TestResult = "PASS"  # 如果不报错，测试通过
        except AssertionError as e:
            print("接口错误，错误是{}".format(e))
            TestResult = "Fail"  # 如果报错了，测试不通过
        finally:  # 不管测试结果是否正确，都把结果写入文件
            self.logger.info("*********开始写入结果********")
            self.t.write_back(item["case_id"] + 1, 8, str(res.json()["message"]))  # 写入实际结果
            self.t.write_back(item["case_id"] + 1, 9, TestResult)  # 写入测试结果
            self.logger.info("*********结束写入数据********")
        # print(res.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

