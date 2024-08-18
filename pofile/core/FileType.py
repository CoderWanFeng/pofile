import os
import pathlib
import shutil
import zipfile
from pathlib import Path

import openpyxl
import psutil
from poprogress import simple_progress


# import requests


class MainFile():

    def replace4filename(self, path: str, del_content: str, replace_content: str = '', dir_rename: bool = True,
                         file_rename: bool = True, suffix=None):
        """
        :param path: 需要替换的文件夹路径
        :param del_content: 需要删除/替换的内容
        :param replace_content: 替换后的内容，可以不填 = 直接删除
        :return:
        """
        pre_list = []
        # file_amonut = 0
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                dir_path = Path(os.path.join(root, dir)).absolute()
                pre_list.append(dir_path)
            for file in files:
                file_path = Path(os.path.join(root, file)).absolute()
                pre_list.append(file_path)
        sub = 0
        for _ in range(len(pre_list)):
            for root, dirs, files in os.walk(path):
                sub += 1
                if dir_rename:
                    for dir in dirs:
                        dir_path = Path(os.path.join(root, dir)).absolute()
                        new_dir_name = dir_path.name.replace(del_content, replace_content)
                        dir_path.rename(dir_path.parent / new_dir_name)
                if file_rename:
                    for file in files:
                        file_path = Path(os.path.join(root, file)).absolute()
                        if suffix == None:
                            new_file_name = file_path.name.replace(del_content, replace_content)
                            file_path.rename(file_path.parent / new_file_name)
                        if suffix != None and file_path.suffix == suffix:
                            new_file_name = file_path.name.replace(del_content, replace_content)
                            file_path.rename(file_path.parent / new_file_name)
                continue

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
            for FileName in simple_progress(FileNameList):
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
            for FileName in simple_progress(FileNameList):
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
            for FileName in simple_progress(FileNameList):
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
            for file_name in simple_progress(file_name_list):
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
            for file_path in simple_progress(dir_path_list):
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
        for dirpath, dirnames, filenames in simple_progress(os.walk(dir_path)):
            print(dirpath, dirnames, filenames)
            for filename in filenames:
                comp_file.write(os.path.join(dirpath, filename), compress_type=zipfile.ZIP_DEFLATED)

    # def urldownload(self, url, filename, dirname):
    #     """
    #     下载文件到指定目录
    #     :param url: 文件下载的url
    #     :param filename: 要存放的文件名，例如：./test.xls
    #     :param dirname: 要存放的文件夹名，以设备id为名称
    #     :return:
    #     """
    #     filedir = self.temp_dir + dirname + '/'  # 每个设备id，存一个文件夹
    #     down_res = requests.get(url)  # 下载内容
    #     # 判断文件夹是否存在，不存在则创建
    #     if not os.path.exists(filedir):
    #         os.makedirs(filedir)
    #     # 存储下载的文件
    #     with open(filedir + filename, 'wb') as file:
    #         file.write(down_res.content)

    def add_line_by_type(self, add_line_dict, file_path, file_type, output_path):
        for root, dirs, files in simple_progress(os.walk(file_path)):
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

    def get_files(self, path, sub, level, suffix, name):
        result_file_path_name_list = []  # 指定路径下，待转换的docx文件。如果是目录，不递归
        abs_input_path = Path(path).absolute()
        # 如果不存在，则不做处理
        if not abs_input_path.exists():
            print("path does not exist path = " + path)
            return
        # 判断是否是文件
        elif abs_input_path.is_file():
            path = Path(path).absolute()
            result_file_path_name_list.append(str(path))
        # 如果是目录，则遍历目录下面的文件
        elif abs_input_path.is_dir():
            for dirpath, _, filenames in simple_progress(os.walk(str(abs_input_path)),
                                                         desc='collecting conditional files：'):
                for filename in filenames:
                    file_path_name = os.path.join(dirpath, filename)
                    if name == '' and not suffix:
                        result_file_path_name_list.append(file_path_name)
                    elif name in filename or Path(file_path_name).suffix == suffix:
                        result_file_path_name_list.append(file_path_name)
        return result_file_path_name_list

    def zip4dir(self, path):
        base_path_list = os.listdir(path)
        for base_path_list_one in simple_progress(base_path_list):
            start_dir = os.path.join(path, base_path_list_one)
            # 子目录
            print("正在压缩的子目录", start_dir)
            if os.path.isdir(start_dir):
                # zip_yasuo(start_dir)
                file_news = start_dir + '.zip'
                if not os.path.isfile(file_news):
                    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
                    for dir_path, dir_names, file_names in os.walk(start_dir):
                        file_path = dir_path.replace(start_dir, '')
                        file_path = file_path and file_path + os.sep or ''
                        for filename in file_names:
                            z.write(os.path.join(dir_path, filename), file_path + filename)
                    z.close()

    def clean4disk(self, disk_name=None):
        def mkdir_temp(path) -> bool and str:
            abs_path = Path(path).absolute()
            exist = True
            if not abs_path.exists():
                exist = False
                os.makedirs(str(abs_path))
            return exist, str(Path(path).absolute()).strip()

        def clean(base_path):
            output_path = base_path / "clean4disk"
            last_index = 0
            for file_index in range(int(usage.free)):
                try:
                    file_name = f'disk_{file_index}.temp'
                    mkdir_temp(output_path)
                    with open(output_path / file_name, 'w') as temp_file:
                        temp_file.write('0' * 1024 ** 3)
                        last_index = file_index
                except:
                    shutil.rmtree(output_path)
                    break

        # 获取磁盘信息
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            # print(f"磁盘分区：{partition.device}")
            # print(f"总空间：{usage.total / (1024 ** 3):.2f} GB")
            # print(f"已使用空间：{usage.used / (1024 ** 3):.2f} GB")
            # print(f"可用空间：{usage.free / (1024 ** 3):.2f} GB")
            print()
            base_path = Path(partition.device)
            if disk_name:
                base_path = Path(disk_name)
                clean(base_path)
                break
            clean(base_path)
