from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext

import json
import random
import math
import datetime

from models import Activity_520

def wuerling(request):

    # information = request.POST.get('information')
    #
    # print(information)
    #
    # if( True ):
    #      return render_to_response('520.html','"test":999')
    # print('wwwwwwwwwwwwwwwwwwwww')
    return render_to_response('520.html',context_instance=RequestContext(request))

def wuerling_action(request):
    print("0000000000000")
    inf_str = request.POST['information']
    print(inf_str)
    information = json.loads(inf_str)
    print(information)
    phone = information['phone']
    wechat = information['wechat']
    sex = information['sex']
    single = information['single']
    time = datetime.datetime.now()

    # record = ''
    lucknum='000'
    result=''
    try:
        Activity_520.objects.get(phone=phone)
        result = {'lucknum': lucknum, 'statu':0}
        print('111111111')
    except Exception as e:
        while(True):
            random_value = random.randint(000, 999)
            lucknum = '%03d' % random_value
            try:
                Activity_520.objects.get(lucknum=lucknum)
                print('2222222222')
                continue
            except Exception as e1:
                print('3333333333333')
                print(e1)
                break
        Activity_520.objects.create(phone=phone, wechatAccount=wechat, sex=sex, single=single, lucknum = lucknum, time=time)
        print("444444444444444")
        result = {'lucknum': lucknum, 'statu':1}
    print(result)
    return HttpResponse(json.dumps(result))
    # for i in range(0, 20):
    #     random_value = random.randint(000, 999)
    #     random_value = '%03d' % random_value
    #     print(random_value)
    #
    # # print(information)
    # # try:
    # #     j = json.loads(information)
    # # except Exception as e:
    # #     print(e)
    # # print(j['phone'])
    # # print(j)
    # return HttpResponse('{"num":999}')