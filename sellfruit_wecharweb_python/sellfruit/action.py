__author__ = 'chenrenzhan'

from models import *
from datetime import datetime
import copy

def prodeceOrderNo():
    lastOrder = Order.objects.last()
    date_now = datetime.now().date()
    if(lastOrder == None):
        month_day = '%02d%02d' % (date_now.month, date_now.day)
        No = '000'
    else:
        date_order = lastOrder.time.date()
        orderNo = lastOrder.orderNo
        month_day = orderNo[:4]
        No = orderNo[4:]
        if(date_now == date_order):
            No = int(No) + 1
            No = '%03d' % No
        else:
            month_day = '%02d%02d' % (date_now.month, date_now.day)
            No = '000'

    orderNo = month_day + No
    return orderNo


def removeAttr(obj, attr):
    obj_copy = copy.deepcopy(obj)
    obj_copy.__delattr__(attr)
    return obj_copy