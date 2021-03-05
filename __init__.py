# encoding: utf-8
import sys
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')
from file_deal  import clear_filename,get_duration

if __name__ == '__main__':
    # clear_filename(path="F:\cs",prefix="3")
    # clear_filename(path="F:/annie/java_basic", prefix=u"教程-java入门必备-适合初学者的全套完整版教程")
    # clear_filename(path=u"F:\\annie\\尚硅谷\\Spring注解驱动教程(雷丰阳源码级讲解)", prefix=u"尚硅谷_")
    # get_duration(path=u"E:\\annie\\spring security")
    get_duration(path=u"E:\\annie\\spring security")

