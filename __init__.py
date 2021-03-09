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
    # get_duration(path=u"E:\\annie\\spring security",rule={"tp":"num","st":20,"end":35})

    first_cmd=None
    
    # print(111000000000000000001)
    # print(first_cmd)

    # path st end
    rule=None
    for  i in range(0,len(sys.argv)):
        if i==1:
            first_cmd=sys.argv[i]
        if i==2:
            rule={"st":int(sys.argv[i]),"tp":"num"}
        if i==3:
            rule["end"]=int(sys.argv[i])



    # get_duration(path=first_cmd if first_cmd else u"E:\\annie\\spring security")
    get_duration(path=first_cmd if first_cmd else u"E:/annie/mybatis" ,rule=rule)

