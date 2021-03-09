# -*- coding: utf-8 -*-
import yaml
import os
def get_package_path(filepath):
   '''
   为了解决包调用时相对路径不正确的问题 ，该解决方案不是很好，
   :param filepath:
   :return:
   '''
   file_catalog=os.path.dirname(os.path.abspath(__file__))
   return os.path.join(file_catalog,"../../",filepath)
   


def yaml_loader(filepath):
   with open(os.path.join(filepath) , encoding='utf8') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
      return config



