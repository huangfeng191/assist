# encoding: utf-8
import sys
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')
from file_deal  import clear_filename,get_duration,clear_freestyle

from utils import yaml_loader


def yaml_deal(plan=None):
    orders = yaml_loader("order.yaml")
    return orders.get(plan or orders.get("plan"))


if __name__ == '__main__':
    # clear_filename(path="F:\cs",prefix="3")
    # clear_filename(path="F:/annie/java_basic", prefix=u"教程-java入门必备-适合初学者的全套完整版教程")
    # clear_filename(path=u"F:\\annie\\尚硅谷\\Spring注解驱动教程(雷丰阳源码级讲解)", prefix=u"尚硅谷_")
    # get_duration(path=u"E:\\annie\\spring security",rule={"tp":"num","st":20,"end":35})

    first_cmd=None
    
    # print(111000000000000000001)
    # print(first_cmd)

    # path st end

    # command param1 param2 param3

    command=None
    params={}
    for i in range(0, len(sys.argv)):
        if i==1:
            command=sys.argv[i]
        elif i>1:
            k,v=sys.argv[i].split("=")
            params[k]=v

    if command=="yaml":
        params=yaml_deal(params.get("plan"))
        command=params.get("command")





    if command=="get_duration":
        rule=None
        if params.get("st") or params.get("end"):
            rule={
                "st":int(params.get("st")) if params.get("st") else None,
                "end":int(params.get("end")) if params.get("end") else None,
                "tp":params.get("tp","num")
            }
        get_duration(path=params.get("path"),rule=rule)
    elif command=="rename":
        clear_filename(path=params.get("path"), prefix=params.get("prefix"))
    elif command=="freestyle":
        clear_freestyle(path=params.get("path"), prefix=params.get("prefix"),separator=params.get("separator"," "))

