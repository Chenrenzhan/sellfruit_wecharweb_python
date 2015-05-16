#!/usr/bin/python
#encoding=utf-8

from django.db import models

# Create your models here.


class Activity_520(models.Model):
    phone = models.CharField(max_length=11, primary_key=True) #手机号码
    wechatAccount = models.CharField(max_length=50) #微信号
    sex = models.SmallIntegerField(max_length=1) #性别 1-男， 2-女， 0-未公开
    single = models.SmallIntegerField(max_length=1) #单身状况 0-不公开， 1-单身， 2-恋爱中
    lucknum = models.CharField(max_length=3) #抽奖号码
    time = models.DateTimeField(auto_now=False, auto_now_add=False) #时间

    class Meta:
        ordering=['time']