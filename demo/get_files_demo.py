# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/4/1 12:16 
@Description     ：
'''
#pip install pofile
import pofile
files_list = pofile.get_files(path=r'D:\workplace\code\github\pofile\tests',name='pdf',sub=False)
print(files_list)

"""
获取指定路径下的所有文件
:param path: 必填，指定路径
:param name: 可以不填，名字中包含的内容
:param sub: 可以不填，是否获取子文件夹内容
:param level: 可以不填，获取第几层文件夹的内容
:return: 装满文件路径的列表
"""