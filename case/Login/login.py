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

from common.get_cookies import GetCookie

res = getattr(GetCookie, "cookie")
print(res)


