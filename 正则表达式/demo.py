"""
-*- coding:utf-8 -*-
author: Super
Date: 2020/6/9
"""

import re

pattern = r"^[1-9]\d{4,9}$"
while True:
    qq = input("请输入QQ:")
    qq_match = re.search(pattern, qq)
    # print(qq_match)
    # break
    if qq_match:
        print("QQ格式正确!")
        break
    else:
        print("QQ格式错误!")
        break
