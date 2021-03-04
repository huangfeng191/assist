# -*- coding: utf-8 -*-
from utils.file import get_file_length,getFiles
import re
import os

class FilesInfo:

    def __init__(self,path=None):
        self.path=path or []
        self.get_files()
    def get_files(self):
        self.files=getFiles(self.path, isPath=True)
        pass
    def _filter_prefix(self,prefix):
        self.files = filter(lambda x: prefix in x ,self.files)

    def _filter_num(self,st=None,end=None,**args):
        def compare(x):
            base_name=os.path.basename(x)
            sn=re.search(r"[0-9]+",base_name)
            if sn:
                n=sn.group(0)
                if st:
                    if int(n)<st:
                        return False
                if end:
                    if int(n)>end:
                        return False
                    return True
            return False
            # 包含数字 and >=st <=end

        self.files = filter(compare, self.files)

    def get_durations(self):
        num=0
        for f in self.files:
            num+=get_file_length(f)

        return f" {round(num/60)} (minutes)"

    def to_limit_files(self,rules):
        for r in rules:
            if r.get("tp")=="prefix":
                self._filter_prefix(prefix=r.get("prefix"))
            if r.get("tp")=="num":
                self._filter_num(**r)

