# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：CoderWanFeng : https://mp.weixin.qq.com/s/HYOWV7ImvTXImyYWtwADog
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/1 20:02 
@本段代码的视频说明     ：
'''
import os
from pathlib import Path


def replace4filename(path: str, del_content: str, replace_content: str = None, sub=False, level=0,
                     suffix=None):
    """
    :param path: 需要替换的文件夹路径
    :param del_content: 需要删除/替换的内容
    :param replace_content: 替换后的内容，可以不填 = 直接删除
    :return:
    """

    pre_list = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dir_path = Path(os.path.join(root, dir)).absolute()
            pre_list.append(dir_path)
        for file in files:
            file_path = Path(os.path.join(root, file)).absolute()
            pre_list.append(file_path)

    for _ in range(len(pre_list)):
        for dir in dirs:
            dir_path = Path(os.path.join(root, dir)).absolute()
            new_dir_name = dir_path.name.replace(del_content, replace_content)
            dir_path.rename(dir_path.parent / new_dir_name)
        for file in files:
            file_path = Path(os.path.join(root, file)).absolute()
            new_file_name = file_path.name.replace(del_content, replace_content)
            file_path.rename(file_path.parent / new_file_name)

    # 获取该目录下所有文件，存入列表中；不包含子文件夹
    fileList = self.get_files(str(Path(path).absolute()), name=del_content, sub=sub, level=level, suffix=suffix)
    file_amonut = 0
    # todo:修改文件夹
    if fileList:
        for old_file_name in simple_progress(fileList):  # 依次读取该路径下的文件名
            abs_old_file_path = Path(old_file_name)
            if not replace_content:
                replace_content = ''
            new_file_name = abs_old_file_path.name.replace(del_content, replace_content)
            abs_old_file_path.rename(abs_old_file_path.parent / new_file_name)
            file_amonut = file_amonut + 1
    print(f"本次运行共进行了{file_amonut}个文件/文件夹的重命名")
