#!/usr/bin/python
#encoding=utf-8
__author__ = 'chenrenzhan'

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound

from forms import OrderForm
from models import *

import datetime

def orderForm(request):

    if 'search' in request.GET:
        stateFalse = False
        stateTrue = False
        start = '2015/01/01 12:00'
        end = datetime.datetime.strftime(datetime.datetime.now(), "%Y/%m/%d %H:%M")
        if(request.GET['start'] != ''):
            start = request.GET['start']
        if( request.GET['end'] != ''):
            end = request.GET['end']
        if 'stateFalse' in request.GET:
            stateFalse = request.GET['stateFalse']
        if 'stateTrue' in request.GET:
            stateTrue = request.GET['stateTrue']
        print(start == '')
        print('aaaaaaaaaaaaaaaaaaaaa')


        if(stateFalse != stateTrue):
            print('00000000000000000000000')
            if(stateFalse == 'True'):
                orders = Order.objects.filter(time__gte = strToDatetime(start), time__lte = strToDatetime(end),
                                              state = False)
                print('11111111111111111111')
            if(stateTrue == 'True'):
                orders = Order.objects.filter(time__gte = strToDatetime(start), time__lte = strToDatetime(end),
                                              state = True)
                print('222222222222222')
        else:
            orders = Order.objects.filter(time__gte = strToDatetime(start), time__lte = strToDatetime(end))
            print('33333333333333333333333')
            print(len(orders))

        orderForms = []
        appleTotal = 0
        bananaTotal = 0
        pearTotal = 0
        lemonTotal = 0

        if(len(orders) == 0):
            return render_to_response('manage.html')
        else:
            for order in orders:
                orderNo = order.orderNo
                allup = json.loads(order.allup)
                appleSum = allup['allup'][0]['list']['amount']
                appleTotal += int(appleSum)
                applePrice = allup['allup'][0]['list']['price']
                appleMeasure = allup['allup'][0]['list']['measurement']
                apple = u'%s%s(%.2f斤)' % (appleSum, measurement(appleMeasure), applePrice)

                bananaSum = allup['allup'][1]['list']['amount']
                bananaTotal += int(bananaSum)
                bananaPrice = allup['allup'][1]['list']['price']
                bananaMeasure = allup['allup'][1]['list']['measurement']
                banana = u'%s%s(%.2f斤)' % (bananaSum, measurement(bananaMeasure), bananaPrice)

                pearSum = allup['allup'][2]['list']['amount']
                pearTotal += int(pearSum)
                print(pearSum + 'pearSum')
                print((pearTotal))
                pearPrice = allup['allup'][2]['list']['price']
                pearMeasure = allup['allup'][2]['list']['measurement']
                pear = u'%s%s(%.2f斤)' % (pearSum, measurement(pearMeasure), pearPrice)

                lemonSum = allup['allup'][3]['list']['amount']
                lemonTotal += int(lemonSum)
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
        return render_to_response('manage.html', {'orders':orderForms, 'appleTotal':appleTotal,
                                                  'bananaTotal':bananaTotal, 'pearTotal':pearTotal,
                                                  'lemonTotal':lemonTotal})

    elif 'change' in request.GET:
        orderNoList = request.GET.getlist('orderNo')
        statesList = request.GET.getlist('state')
        for index, orderNo in enumerate(orderNoList):
            order = Order.objects.get(orderNo = orderNo)
            if(statesList[index] == 'False'):
                order.state = False
            else:
                order.state = True
            order.save()

    return render_to_response('manage.html')

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

#字符串转datetime
def strToDatetime(str):
    return datetime.datetime.strptime(str,"%Y/%m/%d %H:%M")


#encoding=utf-8

# import xlwt
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.db import connection


# def save_asset_xls(request):
#         sql = 'select * from book';
#
#         cursor = connection.cursor()
#         cursor.execute(data_sql)
#         row_all = cursor.fetchall()
#
#         _lst = []
#         _lst.extend(row_all[:])
#         _lst.insert(0, ['列1', '列2', '列3'])
#
#         book = xlwt.Workbook(encoding='utf8')
#         sheet = book.add_sheet('untitled')
#
#         for row, rowdata in enumerate(_lst):
#             for col, val in enumerate(rowdata):
#                 sheet.write(row, col, val, style=xlwt.Style.default_style)
#
#         response = HttpResponse(mimetype='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename=example.xls'
#         book.save(response)
#         return response
