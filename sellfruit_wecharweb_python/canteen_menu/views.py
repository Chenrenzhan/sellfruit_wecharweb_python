#!/usr/bin/python
#encoding=utf-8

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

def canteenmenu(request):

    #1_0, 1_1, 1_2, 1_3, 1_4,分别表示一楼的鸡鸭及其他类,猪肉类,鱼类,素菜类,汤类
    #2_0, 2_1, 2_2, 2_3,分别表示二楼的鸡鸭及其他类,猪肉类,鱼类,素菜类

    
    menus = {
        '1_0':[
            {'name': '烧鸭', 'price': 2.5}, {'name': '辣子鸡', 'price': 3},{'name': '手撕鸡', 'price': 2.5},
        ],
        '1_1':[
            {'name': '手撕鸡', 'price': 2.5},{'name': '木须肉', 'price': 2.5},{'name': '炒三丝', 'price': 3.0},
            {'name': '叉烧', 'price': 3.0},{'name': '红烧土豆', 'price': 2.5},{'name': '咖喱土豆', 'price': 2.5},
            {'name': '水煮肉片', 'price': 3.0},{'name': '粉丝肉丸', 'price': 3.0},{'name': '糖醋排骨', 'price': 4.0},
            {'name': '咸蛋肉饼', 'price': 3.0},{'name': '香干炒肉', 'price': 2.0},{'name': '西兰花炒肉', 'price': 3.0},
            {'name': '豆角炒叉烧', 'price': 3.0},{'name': '荷兰豆炒肉', 'price': 3.0},{'name': '糖醋鸡米花', 'price': 3.0},
            {'name': '红烧狮子头', 'price': 3.0},{'name': '青瓜炒肉片', 'price': 2.5},{'name': '莲藕炒肉片', 'price': 2.5},
            {'name': '莴笋炒肉片', 'price': 2.5},{'name': '黄豆芽炒肉', 'price': 2.0},{'name': '莲藕焖猪手', 'price': 3.0},
            {'name': '玉米粒炒肉丁', 'price': 3.0},
        ],
        '1_2':[
            {'name': '菊花鱼', 'price': 3.0},{'name': '鱼香茄子', 'price': 2.5},{'name': '鱼香肉丝', 'price': 3.0},
            {'name': '蒸塘虱鱼', 'price': 2.0},{'name': '清蒸鱼块', 'price': 2.5},{'name': '麻辣酸菜鱼', 'price': 3.0},
            {'name': '腐竹焖鱼块', 'price': 4.0},
        ],
        '1_3':[
            {'name': '包菜', 'price': 0.5},{'name': '绿豆芽', 'price': 0.5},{'name': '蒸水蛋', 'price': 1.5},
            {'name': '酿豆腐', 'price': 2.5},{'name': '酿茄瓜', 'price': 2.5},{'name': '酿莲藕', 'price': 2.5},
            {'name': '菲菜炒蛋', 'price': 2.5},{'name': '苦瓜炒蛋', 'price': 2.5},{'name': '节瓜炒蛋', 'price': 2.5},
            {'name': '西红柿炒蛋', 'price': 2.0},{'name': '酸辣土豆丝', 'price': 2.0},{'name': '冬菇扒菜旦', 'price': 4.0},
            {'name': '麻辣豆腐', 'price': 1.5},{'name': '蒜蓉炒青菜', 'price': 1.0},{'name': '红烧日本豆腐', 'price': 3.0},
        ],
        '1_4':[
            {'name': '红老火靓汤', 'price': 1.0},{'name': '海底椰炖老鸡', 'price': 6.0}, {'name':'红枣杞子炖乌鸡', 'price':5.0},
            {'name': '杞子淮山炖排骨', 'price': 6.0},
        ],
        '2_0':[
            {'name': '辣子鸡', 'price': 3.0},{'name': '手撕鸡', 'price': 3.0},{'name': '蒸鸡扒', 'price': 3.5},
            {'name': '烧鸭', 'price': 2.5},{'name': '冬菇蒸鸡', 'price': 4.0},{'name': '香煎鸡胸肉', 'price': 5.0},
        ],
        '2_1':[
            {'name': '香芋扣肉', 'price': 3.0},{'name': '莲藕炒肉', 'price': 2.5},{'name': '糖醋里脊', 'price': 4.0},
            {'name': '香干炒肉', 'price': 2.0},{'name': '水煮肉片', 'price': 3.0},{'name': '咖喱土豆', 'price': 2.5},
            {'name': '肉末包菜丝', 'price': 1.5},{'name': '青瓜炒肉片', 'price': 2.0},{'name': '黄豆芽炒肉', 'price': 2.0},
            {'name': '莴笋炒肉片', 'price': 2.5},{'name': '菜花炒腊味', 'price': 2.5},{'name': '花生焖猪手', 'price': 3.0},
            {'name': '红烧狮子头', 'price': 2.5},{'name': '西兰花炒肉', 'price': 3.0},{'name': '糖醋鸡米花', 'price': 3.0},
            {'name': '荷兰豆炒肉', 'price': 3.0},{'name': '豆角炒叉烧', 'price': 3.0},{'name': '木耳蒸排骨', 'price': 3.5},
            {'name': '红烧肉', 'price': 2.5},{'name': '玉米粒炒肉丁', 'price': 3.0},
        ],
        '2_2':[
            {'name': '蒸塘虱鱼', 'price': 2.0},{'name': '包心鱼丸', 'price': 2.5},{'name': '清蒸鱼块', 'price': 2.5},
            {'name': '菊花鱼', 'price': 3.0},{'name': '腐竹焖鱼块', 'price': 3.0},
        ],
        '2_3':[
            {'name': '冬瓜', 'price': 0.5},{'name': '包菜', 'price': 0.5},{'name': '节瓜粉丝', 'price': 2.0},
            {'name': '绿豆芽', 'price': 0.5},{'name': '蒸水蛋', 'price': 1.5},{'name': '酿莲藕', 'price': 2.5},
            {'name': '酿豆腐', 'price': 2.5},{'name': '酿苦瓜', 'price': 2.5},{'name': '酿茄瓜', 'price': 2.5},
            {'name': '蒜蓉生菜', 'price': 1.0},{'name': '麻辣豆腐', 'price': 1.5},{'name': '苦瓜炒蛋', 'price': 2.5},
            {'name': '上汤娃娃菜', 'price': 2.0},{'name': '西红柿炒蛋', 'price': 2.0},{'name': '酸辣土豆丝', 'price': 2.0},
            {'name': '蒜蓉炒上海青', 'price': 1.0},{'name': '蒜蓉炒小白菜', 'price': 1.0},{'name': '红烧日本豆腐', 'price': 3.0},
            {'name': '菲菜炒蛋', 'price': 2.5},
        ],
    }
    return render_to_response('canteen_mune.html', menus)

'''
    menu = {"menus":[
        {'name': '莲藕炒肉片', 'price': 2.5},{'name': '腐竹焖鱼块', 'price': 4},{'name': '冬菇扒菜旦', 'price': 4},
        {'name': '红烧狮子头', 'price': 3},{'name': '莲藕焖猪手', 'price': 3},{'name': '麻辣酸菜鱼', 'price': 3},
        {'name': '菊花鱼', 'price': 3},{'name': '辣子鸡', 'price': 3},{'name': '炒三丝', 'price': 3},
        {'name': '咸蛋肉饼', 'price': 3}, {'name': '粉丝肉丸', 'price': 3},{'name': '椒盐泥鳅', 'price': 3},
        {'name': '糖醋排骨', 'price': 4},{'name': '水煮肉片', 'price': 3},{'name': '鱼香肉丝', 'price': 3},
        {'name': '西兰花炒肉', 'price': 3},{'name': '豆角炒叉烧', 'price': 3},{'name': '荷兰豆炒肉', 'price': 3},
        {'name': '糖醋鸡米花', 'price': 3},{'name': '玉米粒炒肉丁', 'price': 3},{'name': '红烧日本豆腐', 'price': 3},
        {'name': '鸡柳', 'price': 3.5},{'name': '叉烧', 'price': 3},{'name': '烧鸭', 'price': 2.5},
        {'name': '酿豆腐', 'price': 2.5},{'name': '酿苦瓜', 'price': 2.5},{'name': '酿茄瓜', 'price': 2.5},
        {'name': '酿莲藕', 'price': 2.5},{'name': '木须肉', 'price': 2.5}, {'name': '手撕鸡', 'price': 2.5},
        {'name': '红烧土豆', 'price': 2.5},{'name': '咖喱土豆', 'price': 2.5},{'name': '鱼香茄子', 'price': 2.5},
        {'name': '韭菜炒蛋', 'price': 2.5},{'name': '苦瓜炒蛋', 'price': 2.5},{'name': '清蒸鱼块', 'price': 2.5},
        {'name': '青瓜炒肉片', 'price': 2.5},{'name': '莴笋炒肉片', 'price': 2.5},{'name': '西红柿炒蛋', 'price': 2},
        {'name': '酸辣土豆丝', 'price': 2},{'name': '黄豆芽炒肉', 'price': 2},{'name': '蒜蓉炒青菜', 'price': 1},
        {'name': '香干炒肉', 'price': 2},{'name': '蒸塘虱鱼', 'price': 2},{'name': '麻辣豆腐', 'price': 1.5},
        {'name': '包菜', 'price': 0.5},{'name': '蒸水蛋', 'price': 1.5},{'name': '绿豆芽', 'price': 1},
        {'name': '杞子淮山炖排骨(汤)', 'price': 6}, {'name': '红枣杞子炖乌鸡(汤)', 'price': 5},{'name': '杞子淮山炖排骨(汤)', 'price': 6},
        {'name': '红老火靓汤(汤)', 'price': 1},{'name': '海底椰炖老鸡(汤)', 'price': 6},
    ],}
    print(menu)
    return render_to_response('canteen_mune.html', menu)
'''
"""
    #ajax通讯
    condition = request.POST.get('condition')

    if(condition == '0-0'):
        return HttpResponse(json.dumps(menu))
"""
