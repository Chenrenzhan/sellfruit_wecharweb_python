#!/usr/bin/python
#encoding=utf-8
__author__ = 'chenrenzhan'

from django import forms
from django.forms import ModelForm
from models import *

class BuyFoorm(forms.Form):
    apple = forms.IntegerField(required=False)
    banana = forms.IntegerField(required=False)
    pear = forms.IntegerField(required=False)
    lemon = forms.IntegerField(required=False)

    # orderNo = forms.CharField(max_length=7) #订单编号，由日期和三位编号组成，如0402005
    # user = forms.FreignKey(User) #用户信息
    # allup = forms.TextField() #总的水果数量，把各种水果的量和价格构建成json对象，如：{“apple":{"price":"2.5","amount":"3","measurement":"0"},"banana":....}
    # price-单价；amount-数量；measurement-称量方式，1-以“个”算，0-以“斤”算
    # allmoney = forms.FloatField(null=True) #总金额
    # delivery = forms.BooleanField(default=True) #配送方式，true-自取，false-送到宿舍
    # state = forms.BooleanField(default=False) #状态，true-已经配送，false-还没配送
    # phone = forms.CharField(max_length=11) #手机号码
    # dorm = forms.CharField(max_length=4) #宿舍号
    # remarks = forms.TextField(blank=True) #备注
    # time = forms.DateTimeField(auto_now=True, auto_now_add=False) #生成订单的时间

class OrderForm(forms.Form):
    delivery = forms.BaseForm()
    dorm = forms.CharField(max_length=4, required=False)
    phone = forms.CharField(max_length=11)


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=forms.Textarea)


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ('oderNo', 'phone', 'dorm', )