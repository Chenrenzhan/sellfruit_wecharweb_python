#!/usr/bin/python
#encoding=utf-8
__author__ = 'chenrenzhan'

from django.shortcuts import render_to_response
from models import *

def queryorder(request):
    if 'query' in request.GET:
        phone = request.GET['phone']
        type = request.GET['type']

        orderForms = []
        orders = []
        orderList = Order.objects.filter(phone = phone)
        if(len(orderList) == 0):
            return render_to_response('queryorder.html',{'orders':orderForms, 'total':len(orders),})
        else:
            #最近
            if(type == 'true'):
                print(type)
                print(orderList[0])
                orders.append(orderList[0])

            else:
                orders = orderList
            print(orders[0].orderNo)
            fruitName = ['苹果', '香蕉', '雪梨', '柠檬', '芒果', '火龙果']
            for order in orders:
                time = order.time.strftime('%Y-%m-%d %H:%M')
                allup = json.loads(order.allup)
                # sum = {0, 0, 0, 0, 0, 0}
                fruit = []
                for index in range(len(allup['allup'])):
                    sum = allup['allup'][index]['list']['amount']
                    fruit.append({'name': fruitName[index], 'sum':int(sum)})
                # apple = allup['allup'][0]['list']['amount']
                # banana = allup['allup'][1]['list']['amount']
                # pear = allup['allup'][2]['list']['amount']
                # lemon = allup['allup'][3]['list']['amount']
                # mango = allup['allup'][4]['list']['amount']
                # pitaya = allup['allup'][5]['list']['amount']
                delive = delivery(order.delivery)
                st = state(order.state)
                print(delive)
                orderForms.append({'time':time, 'fruits':fruit, 'delivery':delive, 'state':st,})
        return render_to_response('queryorder.html',{'orders':orderForms, 'total':len(orders),})

    return render_to_response('queryorder.html', {'tatol':0})


def delivery(deli):
    if(deli == True):
        return u'自取'
    else:
        return u'送到宿舍'

def state(state):
    if(state == True):
        return 1
    else:
        return 0