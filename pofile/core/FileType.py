import os
import zipfile

import requests
from alive_progress import alive_bar

import pathlib
import openpyxl


class MainFile():

    def replace4filename(self, path, del_content, replace_content):
        """
        :param path: 需要替换的文件夹路径
        :param del_content: 需要删除/替换的内容
        :param replace_content: 替换后的内容，可以不填 = 直接删除
        :return:
        """
        # 获取该目录下所有文件，存入列表中；不包含子文件夹
        fileList = os.listdir(path)
        work_count = 0
        with alive_bar(len(fileList)) as bar:
            for old_file_name in fileList:  # 依次读取该路径下的文件名
                bar()  # 进度条
                if del_content in old_file_name:

                    if replace_content:
                        new_file_name = old_file_name.replace(del_content, replace_content)
                    else:
                        new_file_name = old_file_name.replace(del_content, '')
                    os.rename(path + os.sep + old_file_name, path + os.sep + new_file_name)
                    work_count = work_count + 1
        print("当前目录下，共有{}个文件/文件夹，本次运行共进行了{}个文件/文件夹的重命名".format(len(fileList), work_count))

    # @time_count_dec
    def file_name_insert_content(self, file_path, insert_position: int, insert_content: str):
        """

        :param file_path: 文件存放路径
        :param insert_position: 插入位置（内容将插入在此之后，如果输入位置大于文件主名长度将插入在末尾）
        :param insert_content: 插入内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    FileNameExtension = "".join(list(FileName.suffixes))
                    FileNameRoot = FileName.name.replace(FileNameExtension, "")
                    # 分离文件主名和扩展名，防止对扩展名进行操作
                    FileNameFormer = FileNameRoot[:insert_position:]
                    FileNameLatter = FileNameRoot[insert_position::]
                    # 拆分文件主名
                    NewFileName = FileNameFormer + insert_content + FileNameLatter + FileNameExtension  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    # @time_count_dec
    def file_name_add_prefix(self, file_path, prefix_content: str):
        """

        :param file_path: 文件存放路径
        :param prefix_content: 前缀内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    NewFileName = prefix_content + FileName.name  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    # @time_count_dec
    def file_name_add_postfix(self, file_path, postfix_content: str):
        """

        :param file_path: 文件存放路径
        :param postfix_content: 后缀内容
        """
        Path = pathlib.Path(file_path).resolve()
        if Path.is_dir():
            FileNameList = list(Path.glob("*"))  # 获取该路径下的文件列表
            for FileName in FileNameList:
                if FileName.is_file():  # 判断是否为文件，只对文件进行操作
                    FileNameExtension = "".join(list(FileName.suffixes))
                    FileNameRoot = FileName.name.replace(FileNameExtension, "")
                    # 分离文件主名和扩展名
                    NewFileName = FileNameRoot + postfix_content + FileNameExtension  # 合并文件名
                    if not Path.joinpath(NewFileName).is_file():
                        FileName.rename(Path.joinpath(NewFileName))
                    else:
                        print(f"该目录下已存在名为{NewFileName}的文件，请检查！")
        else:
            print("请输入文件夹路径")

    def search_specify_type_file(self, file_path, file_type: str):
        '''

        :param file_path:目标路径
        :param file_type:需要查找的文件类型
        '''
        print("开始查找")
        i = 0  # 计数变量
        file_path = pathlib.Path(file_path).resolve()
        if file_path.is_dir():
            file_name_list = list(file_path.glob("**/*"))  # 获取该路径下的文件列表
            for file_name in file_name_list:
                file_name_extension = "".join(list(file_name.suffixes))
                if file_name_extension == file_type:
                    print(f"{file_name.name}，{file_name.parent}")
                    i = i + 1
            print(f"查找完成，共找到{i}个文件")
        else:
            print("请输入文件夹路径")

    def output_file_list_to_excel(self, dir_path: str):
        """
        :param dir_path: 需要生成文件列表的目录
        """
        dir_path = pathlib.Path(dir_path).resolve()
        if dir_path.is_dir():
            dir_path_list = list(dir_path.glob("**/*"))
            output_excel = openpyxl.Workbook()
            output_excel_sheet = output_excel.active
            output_excel_sheet.append(["完整路径", "文件所在路径", "文件名"])
            for file_path in dir_path_list:
                if file_path.is_file():
                    output_excel_sheet.append([str(file_path), str(file_path.parent), str(file_path.name)])
            output_excel.save(dir_path.joinpath("本目录文件列表.xlsx"))
        else:
            print("请输入正确的文件路径！")

    # 清空指定目录
    def del_dirs(self, dir_path):
        for root, dirs, files in os.walk(dir_path, topdown=False):
            # 删除文件
            for name in files:
                os.remove(os.path.join(root, name))  # 删除文件
            # 删除空文件夹
            for name in dirs:
                os.rmdir(os.path.join(root, name))  # 删除一个空目录

    # 压缩指定目录的文件
    def zip_dir(self, dir_path):
        comp_file = zipfile.ZipFile(str(dir_path), 'w')  # 文件的压缩
        for dirpath, dirnames, filenames in os.walk(dir_path):
            print(dirpath, dirnames, filenames)
            for filename in filenames:
                comp_file.write(os.path.join(dirpath, filename), compress_type=zipfile.ZIP_DEFLATED)

    def urldownload(self, url, filename, dirname):
        """
        下载文件到指定目录
        :param url: 文件下载的url
        :param filename: 要存放的文件名，例如：./test.xls
        :param dirname: 要存放的文件夹名，以设备id为名称
        :return:
        """
        filedir = self.temp_dir + dirname + '/'  # 每个设备id，存一个文件夹
        down_res = requests.get(url)  # 下载内容
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        # 存储下载的文件
        with open(filedir + filename, 'wb') as file:
            file.write(down_res.content)

    def add_line_by_type(self, add_line_dict, file_path, file_type, output_path):
        for root, dirs, files in os.walk(file_path):
            # root 表示当前访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list
            # 遍历文件
            for f in files:
                if str(f).endswith(file_type):
                    f = os.path.join(root, f)
                    for line_num in range(0, len(add_line_dict)):
                        with open(f, 'r') as original: data = original.read()
                        line_num_str = add_line_dict.get(line_num + 1)
                        with open(f, 'w') as modified: modified.write(str(line_num_str) + '\n' + data)
        print(f'【{file_path}】文件夹内，所有后缀为【{file_type}】的文件，都已修改完毕')
