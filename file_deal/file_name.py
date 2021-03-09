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
                files = filter(lambda x:self.prefix in x.decode("gbk").encode("utf-8") , files)
                files = map(lambda x: x.decode("gbk"), files)
            except:
                files = filter(lambda x: self.prefix in x.decode("utf-8").encode("utf-8"), files)
                files = map(lambda x: x.decode("utf-8"), files)
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


def clear_freestyle():
    a = DealName(prefix=u"雷丰阳2021版SpringBoot2零基础入门springboot全套完整版（spring boot2） P")
    files=a._get_with_prefix()
    for f in files:
        pathname = os.path.dirname(f)
        basename=os.path.basename(f)
        deal=basename.encode("utf-8").split("、")[0]
        after=basename.encode("utf-8").split("、")[1]
        if len(deal)==3:
            basename=deal[1:3]+after
        elif len(deal)==4:
            basename = deal[2:4] + after

        print(os.path.join(pathname, basename.decode("utf-8"))) # utf-8 与 unicode 还是有差别的
        os.rename(f, os.path.join(pathname, basename.decode("utf-8")))






    # a.replace_with_sub(discard=" ")
