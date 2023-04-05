#!/usr/bin/env python
# -*- coding:utf-8 -*-
from poprogress import simple_progress

#############################################
# File Name: 文件.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 文件 的自动化操作
#############################################
from pofile.core.FileType import MainFile
from pofile.core.SearchByContentType import MainSearchByContent
import search4file
import os
import shutil
from pathlib import Path

mainFile = MainFile()
mainSearchByContent = MainSearchByContent()


# todo：输入文件路径
# @except_dec()
def replace4filename(path, del_content, replace_content=None):
    mainFile.replace4filename(path, del_content, replace_content)


# todo：输入文件路径
# @except_dec()
def search_by_content(search_path, search_content):  # 定义 search() 函数，传入 "path" 文件路径， "target" 要查找的目标文件
    search4file.search_by_content(search_path, search_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_insert_content(file_path, insert_position: int, insert_content: str):
    mainFile.file_name_insert_content(file_path, insert_position, insert_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_add_prefix(file_path, prefix_content):
    mainFile.file_name_add_prefix(file_path, prefix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/72
# @except_dec()
def file_name_add_postfix(file_path, postfix_content):
    mainFile.file_name_add_postfix(file_path, postfix_content)


# author：https://github.com/CoderWanFeng/python-office/pull/74
# @except_dec()
def search_specify_type_file(file_path, file_type):
    mainFile.search_specify_type_file(file_path, file_type)


# @except_dec()
def output_file_list_to_excel(dir_path):
    mainFile.output_file_list_to_excel(dir_path)


def add_line_by_type(add_line_dict: dict, file_path, file_type='.py', output_path=r'add_line'):
    mainFile.add_line_by_type(add_line_dict, file_path, file_type, output_path)


def group_by_name(path, output_path, del_old_file):
    """
    根据后缀名，整理文件
    :param path:
    :return:
    """
    abs_input_path = Path(path).absolute()  # 相对路径→绝对路径
    if output_path:
        abs_output_path = Path(output_path).absolute()
    else:
        abs_output_path = abs_input_path  # 默认整理结果放在当前文件夹下
    for file in abs_input_path.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            file_extension = file.suffix.split(".")[-1]  # 扩展名
            current_dile_dir = abs_output_path / file_extension
            if Path(current_dile_dir).exists():
                shutil.copy(file, current_dile_dir)  # 复制，不删除源文件
            else:
                Path.mkdir(current_dile_dir)
                shutil.copy(file, current_dile_dir)


def get_files(path: str, name: str = '', suffix: str = None, sub: bool = False, level: int = 0) -> list:  # TODO：全面支持正则
    """
        获取指定路径下的所有文件
    :param path: 必填，指定路径
    :param name: 可以不填，名字中包含的内容
    :param suffix: 可以不填，指定文件后缀
    :param sub: 可以不填，是否获取子文件夹内容
    :param level: 可以不填，获取第几层文件夹的内容
    :return: 装满文件路径的列表
    """

    result_file_path_name_list = mainFile.get_files(path=path, name=name, sub=sub, level=level, suffix=suffix)
    if result_file_path_name_list:
        print(f'files amount:{len(result_file_path_name_list)}')
    else:
        print(f'0 conditional file in {str(Path(path).absolute())}')
    return result_file_path_name_list
