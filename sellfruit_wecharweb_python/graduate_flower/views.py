#!/usr/bin/python
#encoding=utf-8

from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext

import json
import random
import math
import datetime

from models import *

def graduate_flower(request):
    try:
        flower_list = Flower.objects.all()

    except:
        pass

    flowers = []
    for flower in flower_list:
        picture = flower.get_picture()
        aflower = {'flower': flower, 'picture': picture}
        flowers.append(aflower)

    aviable = {'flowers': flowers}
    print(aviable)
    return render_to_response('flower.html',aviable, context_instance=RequestContext(request))

def graduate_flower_action(request):
    ERROR = False
    SECCESS = True
    statu = ERROR
    print("sssssssssssss")
    if ( 'information' not in request.POST):
        statu = ERROR
    else:
        info_str = request.POST['information']
        information = json.loads(info_str)
        print(info_str)
        time = datetime.datetime.now()
        phone = information['phone']
        remark = information['remark']
        has_delivery = False

        total_amount = 0.00
        flowers_list = information['flowers']
        for flower in flowers_list:
            type = flower['type']
            type = int(type) + 1
            print(type)
            try:
                flower_obj = Flower.objects.get(id = type)
                total_amount += flower_obj.flower_price
            except Exception as e:
                print(e)
                continue
        print(total_amount)
        order = None
        try:
            order = FloweraOrder.objects.create(totalamount=float(total_amount), gtime=time, phone=phone, remarks=remark, has_delivery=has_delivery)
            # order.save()
        except Exception as e:
            print(e)
            statu = ERROR
            variable = {'statu': statu}
            return HttpResponse(json.dumps(variable))

        print(order)

        for flower in flowers_list:
            type = flower['type']
            type = int(type) + 1
            flower_obj = None
            try:
                flower_obj = Flower.objects.get(id = type)
                total_amount += flower_obj.flower_price
            except:
                continue
            date = flower['date']
            try:
                order_flower = Order_Flower.objects.create(flower_order=order, flower=flower_obj, take_time=date)
                statu = SECCESS
            except Exception as e:
                print(e)
                statu = ERROR



    variable = {'statu': statu}

    return HttpResponse(json.dumps(variable))
