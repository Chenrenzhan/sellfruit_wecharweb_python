__author__ = 'chenrenzhan'

from models import *
from datetime import datetime
import copy

def prodeceOrderNo():
    lastOrder = Order.objects.last()
    date_now = datetime.now().date()
    month_day_now = '%02d%02d' % (date_now.month, date_now.day)
    if(lastOrder == None):
        month_day = month_day_now
        No = '000'
        print("1111111111")
    else:
        date_order = lastOrder.time.date()
        orderNo = lastOrder.orderNo
        print(orderNo)
        month_day = orderNo[:4]
        print(month_day)
        print(date_now)
        No = orderNo[4:]
        if(month_day_now == month_day):
            No = int(No) + 1
            No = '%03d' % No
            print('2222222222222')
            print(date_now)
            print(date_order)
            print(No)
        else:
            month_day = month_day_now
            No = '000'
            print('333333333333')

    orderNo = month_day + No
    return orderNo


def removeAttr(obj, attr):
    obj_copy = copy.deepcopy(obj)
    obj_copy.__delattr__(attr)
    return obj_copy