# -*- coding: utf-8 -*-
from utils.file import getFiles
import os



class DealName:
    def __init__(self,prefix,path="./"):
        self.prefix=prefix
        self.path=path
    def _get_with_prefix(self):
        files=getFiles(self.path, isPath=True)
        if self.prefix:
            try:
                files = filter(lambda x:self.prefix in x , files)

            except:
               raise Exception("i don't know ")
        return files
    def file_replace(self,f,str=None):
        if not str:
            str = self.prefix
        pathname = os.path.dirname(f)
        basename = os.path.basename(f).replace(str, "", 1)
        print (pathname, basename)
        os.rename(f, os.path.join(pathname,basename))
    def replace_with_str(self):
        '''
        直接根据prefix 截取文件名
        :return:
        '''
        files = self._get_with_prefix()
        for f in files:
            self.file_replace(f)

    def replace_with_sub(self, discard,str=None):
        '''
              根据prefix 截取文件名 ,sub
             :return:
             '''
        files = self._get_with_prefix()
        if not str:
            str = self.prefix
        for f in files:
            pathname = os.path.dirname(f)
            basename =os.path.basename(f).replace(str, "", 1)
            if discard in basename:
                basename =basename.replace(discard, "", 1)
                print (pathname,basename)
                os.rename(f, os.path.join(pathname, basename))
        '''
         prefix + sub.split(str) 1 获取
        :param str:
        :return:
        '''
        pass

def clear_prefix():
    a = DealName(prefix=u"雷丰阳2021版SpringBoot2零基础入门springboot全套完整版（spring boot2） P")
    a.replace_with_sub(discard=" ")








    # a.replace_with_sub(discard=" ")
