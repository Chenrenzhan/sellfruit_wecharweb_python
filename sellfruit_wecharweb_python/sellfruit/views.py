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
        {"type":"apple","list":apple, 'comment': 'http://127.0.0.1:8000/comment/appple/',},
        {"type":"banana","list":banana, 'comment': 'http://127.0.0.1:8000/comment/banana/'},
        {"type":"pear","list":pear, 'comment': 'http://127.0.0.1:8000/comment/pear/'},
        {"type":"lemon","list":lemon, 'comment': 'http://127.0.0.1:8000/comment/lemon/'}
    ], }

    comment = {'apple':apple, 'banana': banana, 'pear': pear, 'lemon': lemon}
    request.session['comment'] = comment

    if 'fruitSum' in request.GET:
        fruitSum =  request.GET.getlist('fruitSum')
        request.session['fruits'] = fruitSum #把选购水果的数量存到session
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
            apple.amount += int(fruits[0])
            apple.save()
            banana.amount += int(fruits[1])
            banana.save()
            pear.amount += int(fruits[2])
            pear.save()
            lemon.amount += int(fruits[3])
            lemon.save()

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

def comment(request, url):
    apple = Comment.objects.filter(fruit_id = 1)
    banana = Comment.objects.filter(fruit_id = 2)
    pear = Comment.objects.filter(fruit_id = 3)
    lemon = Comment.objects.filter(fruit_id = 4)

    validate = {'fruit':apple[0], 'comment': apple}

    path = request.path
    if(path == '/comment/apple/'):
        validate = {'fruit':apple[0], 'comment': apple}
    elif(path == '/comment/banana/'):
        validate = {'fruit':banana[0], 'comment': banana}
    elif(path == '/comment/pear/'):
        validate = {'fruit':pear[0], 'comment': pear}
    elif(path == '/comment/lemon/'):
        validate = {'fruit':lemon[0], 'comment': lemon}
    return render_to_response('comment.html', validate)

def toComment(request):
    return render_to_response('myComment.html')