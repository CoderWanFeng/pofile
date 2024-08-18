# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/3/11 21:11 
@本段代码的视频说明     ：
'''
import shutil
from pathlib import Path

import psutil

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
    output_path = base_path / "clean4disk"
    last_index = 0
    for file_index in range(int(usage.free)):
        try:
            file_name = f'disk_{file_index}.temp'
            with open(output_path / file_name, 'w') as temp_file:
                temp_file.write('0' * 1024 ** 3)
                last_index = file_index
        except:
            shutil.rmtree(output_path)
            break
