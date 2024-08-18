# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/8x7c9qiAneTsDJq9JnWLgA
@个人网站 ：www.python-office.com
@Date    ：2023/7/3 23:18 
@Description     ：
'''

import difflib

with open("a.txt", "r") as file:
    file1_data = file.readlines()

with open("b.txt", "r") as file:
    file2_data = file.readlines()

differ = difflib.Differ()
diff = list(differ.compare(file1_data, file2_data))
print(diff)
with open("diff.txt", "w") as file:
    file.writelines(diff)