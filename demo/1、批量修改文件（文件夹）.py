

# 集成使用
import office

office.file.replace4filename(path='./add', del_content='add', replace_content='plus', dir_rename=False,
                             file_rename=False, suffix='.py')
# 单独使用
import pofile

pofile.replace4filename(path='./add', del_content='add', replace_content='plus', dir_rename=False, file_rename=False,
                        suffix='.py')
