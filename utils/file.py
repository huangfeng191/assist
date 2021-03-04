# -*- coding: utf-8 -*-
import json,os
from utils import get_package_path
from moviepy.editor import VideoFileClip
def get_file_json(file):
    with open(file) as f:
        a=f.read()
        return json.loads(a)



# 保存内容到文件
def save_file(file_path,content):
    fpath, _ = os.path.split(file_path)  # 分离文件名和路径
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    with open(file_path, 'w') as f:
            f.write(content)
    return "OK"




def getFiles (srcPath,postfix=None,isPath=False,local=None):
    '''
    :param 根据路径获取文件，不包括目录:
    :param postfix:  .md
    :param isPath: True 输出完整路径
    :return:
    '''

    if local == "local":
        srcPath= get_package_path(srcPath)

    aFiles = [x for x in os.listdir(srcPath) if
              os.path.isfile(os.path.join(srcPath, x)) ]

    def not_empty(s):
        if os.path.splitext(s)[1]==postfix:
            return True
        else:
            return False
    if postfix:
        aFiles=filter(not_empty,aFiles)
    if isPath:
        def f(x):
            return os.path.join(srcPath, x)
        aFiles=map(f,aFiles)

    return aFiles



def get_file_length(filename):
    clip = VideoFileClip(filename)

    return clip.duration