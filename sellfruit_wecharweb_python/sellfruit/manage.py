#!/usr/bin/python
#encoding=utf-8
__author__ = 'chenrenzhan'

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound

from forms import OrderForm
from models import *

def orderForm(request):
    orders = Order.objects.all()
    orderForms = []
    if(len(orders) == 0):
        return HttpResponse('没有订购记录！')
    else:
        for order in orders:
            orderNo = order.orderNo
            allup = json.loads(order.allup)
            # print(allup)
            # print('allup[0].list.amount')
            # print(allup[0].list.price)
            appleSum = allup['allup'][0]['list']['amount']
            applePrice = allup['allup'][0]['list']['price']
            appleMeasure = allup['allup'][0]['list']['measurement']
            # print(u'fff%s' % appleSum)
            # print( measurement(appleMeasure))
            # print(u'%s%s(%.2f斤)' % (appleSum, measurement(appleMeasure), applePrice))
            apple = u'%s%s(%.2f斤)' % (appleSum, measurement(appleMeasure), applePrice)

            bananaSum = allup['allup'][1]['list']['amount']
            bananaPrice = allup['allup'][1]['list']['price']
            bananaMeasure = allup['allup'][1]['list']['measurement']
            banana = u'%s%s(%.2f斤)' % (bananaSum, measurement(bananaMeasure), bananaPrice)

            pearSum = allup['allup'][2]['list']['amount']
            pearPrice = allup['allup'][2]['list']['price']
            pearMeasure = allup['allup'][2]['list']['measurement']
            pear = u'%s%s(%.2f斤)' % (pearSum, measurement(pearMeasure), pearPrice)

            lemonSum = allup['allup'][3]['list']['amount']
            lemonPrice = allup['allup'][3]['list']['price']
            lemonMeasure = allup['allup'][3]['list']['measurement']
            lemon1 = u'%s%s(%.2f斤)' % (lemonSum, measurement(lemonMeasure), lemonPrice)

            phone = order.phone
            dorm = order.dorm
            deliv = delivery(order.delivery)
            st = state(order.state)
            time = order.time
            print(time)
            orderForms.append(
                OrderForm({'orderNo': orderNo, 'apple': apple, 'banana': banana, 'pear': pear, 'lemon': lemon1,
                          'phone': phone, 'dorm': dorm, 'delivery': deliv, 'state': st,
                          'time': time})
            )
    print(orderForms)
    return render_to_response('manage.html', {'orders':orderForms})

def measurement(measure):
    if(measure == 0):
        return u'斤'
    else:
        return u'个'

def delivery(deli):
    if(deli == True):
        return u'自取'
    else:
        return u'送到宿舍'

def state(state):
    if(state == True):
        return u'已配送'
    else:
        return u'未配送'



