
# -*- coding: utf-8 -*-
from file_deal.file_name import DealName
from file_deal.file_info import FilesInfo
import os

def clear_filename(prefix="11",path="./"):
    '''
    将文件名中的固定字符删除
    :param prefix: 现需要替换的字符串
    :param path: 需要替换的路径，目前只支持1层目录
    :return:
    '''
    a = DealName(prefix=prefix,path=path)
    a.replace_with_str()
    print ("OK")


def get_duration(path,rule=None):

    rules=[
        # {"tp":"num","st":20,"end":35}
    ]
    if rule:
        rules.append(rule)
    fs=FilesInfo(path)
    fs.to_limit_files(rules)
    print(fs.get_durations())

def clear_freestyle(prefix="11",path="./",separator=" "):
    '''
    只支持  a[1] 截取 separator
    :param prefix:
    :param path:
    :return:
    '''
    a = DealName(prefix=prefix,path=path)
    files=a._get_with_prefix()
    for f in files:
        pathname = os.path.dirname(f)
        basename=os.path.basename(f)
        deal=basename.split(separator)[0]
        after=basename.split(separator)[1]

        basename=after


        print(os.path.join(pathname, basename)) # utf-8 与 unicode 还是有差别的
        os.rename(f, os.path.join(pathname, basename))
