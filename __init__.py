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

    first_cmd=None
    


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

