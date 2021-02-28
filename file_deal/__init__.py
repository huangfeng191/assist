
# -*- coding: utf-8 -*-
from file_deal.fine_name import DealName


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