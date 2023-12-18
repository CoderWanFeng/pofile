# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/1 21:01 
@本段代码的视频说明     ： https://www.bilibili.com/video/BV12r4y187Yj
'''

# 集成使用
import office

office.file.replace4filename(path='./add', del_content='add', replace_content='plus', dir_rename=False,
                             file_rename=False, suffix='.py')
# 单独使用
import pofile

pofile.replace4filename(path='./add', del_content='add', replace_content='plus', dir_rename=False, file_rename=False,
                        suffix='.py')
