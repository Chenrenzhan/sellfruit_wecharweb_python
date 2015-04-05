#!/usr/bin/python
#encoding=utf-8

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import copy

from models import *
from action import *

# Create your views here.

def index(request):
    #从数据库读取数据
    apple = Fruit.objects.get(fruitType=1) #从数据库读取苹果数据
    banana = Fruit.objects.get(fruitType=2)
    pear = Fruit.objects.get(fruitType=3)
    lemon = Fruit.objects.get(fruitType=4)
    validate = {"fruits": [
        {"type":"apple","list":apple}, {"type":"banana","list":banana},
        {"type":"pear","list":pear}, {"type":"lemon","list":lemon}
    ], }

    if 'fruitSum' in request.GET:
        fruitSum =  request.GET.getlist('fruitSum')



        request.session['fruits'] = fruitSum
        #return HttpResponse(fruits['fruits'][0]['name'])
        return HttpResponseRedirect('/order/')
        # return render_to_response('order.html', {'fruitslist':request.GET.getlist('fruitSum')})
        # HttpResponse(request.GET.getlist('fruitSum')[0])
    # else:
    #    return HttpResponse
        #return HttpResponse(message)


    return render_to_response('index.html', validate)

def order(request):
    #从数据库读取数据
    apple = Fruit.objects.get(fruitType=1) #从数据库读取苹果数据
    banana = Fruit.objects.get(fruitType=2)
    pear = Fruit.objects.get(fruitType=3)
    lemon = Fruit.objects.get(fruitType=4)

    fruits = request.session['fruits']

    if 'phone' in request.GET and request.GET['phone']:
        delivery = request.GET['del']
        phone = request.GET['phone']
        dorm = request.GET['dorm']

        orderNo = prodeceOrderNo()
        allup = {'allup': [
                     {'type':'apple',
                        'list':{"price":apple.price,"amount":fruits[0],"measurement":apple.measurement}},
                     {'type':'banana',
                        'list':{"price":banana.price,"amount":fruits[1],"measurement":banana.measurement}},
                     {'type':'pear',
                        'list':{"price":pear.price,"amount":fruits[2],"measurement":pear.measurement}},
                     {'type':'lemon',
                        'list':{"price":lemon.price,"amount":fruits[3],"measurement":lemon.measurement}},
        ],}
        allmoney = 0
        state = False
        remarks = ''
        time = datetime.now()
        flag = Order.objects.create(orderNo=orderNo, allup=json.dumps(allup),
                                    allmoney = allmoney, delivery = delivery,
                                    state = state, phone = phone,
                                    dorm = dorm, remarks = remarks,
                                    time = time)
        if(flag):
            #销售重量增加
            apple.amount += fruits[0]
            banana.amount += fruits[1]
            pear.amount += fruits[2]
            lemon.amount += fruits[3]


            return HttpResponseRedirect('/index/')
    # else:
    #     return HttpResponse('not phone')
    rFruits={'orderNo': prodeceOrderNo(), 'fruits':[
            {'name': apple.fruitName, 'measurement': apple.measurement, 'sum': fruits[0]},
            {'name': banana.fruitName, 'measurement': banana.measurement, 'sum':fruits[1]},
            {'name': pear.fruitName, 'measurement': pear.measurement, 'sum':fruits[2]},
            {'name': lemon.fruitName, 'measurement': lemon.measurement, 'sum':fruits[3]}
        ]}

    return render_to_response('order.html',{'fruits':rFruits})

def comment(request):
    return render_to_response('comment.html')

def toComment(request):
    return render_to_response('myComment.html')