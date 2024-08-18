def check_suffix(file_name: str, suffix_list: list) -> bool:
    """
    判断后缀是否为指定类型
    :param file_name: 文件名
    :param suffix_list: 后缀名的列表
    :return: True/False
    """
    in_suffix_list = False
    for suffix in suffix_list:
        if file_name.endswith(suffix):
            in_suffix_list = True
            break
    return in_suffix_list


def fix_unsaved_char(file_name: str) -> str:
    """
    修复文件名中有未保存的字符
    :param file_name: 文件名
    :return: 修复后的文件名
    """
    invalid_character = r'<>:"/\|?* '
    for char in invalid_character:
        file_name = file_name.replace(char, '_')
    return file_name.replace('?', '_').replace('*', '_').replace('"', '_').replace(':', '_').replace('<', '_').replace(
        '>', '_').replace('/', '_').replace('\\', '_').replace('|', '_').replace('?', '_').replace('"', '_').replace(
        ':', '_')
