#!/usr/bin/python
#encoding=utf-8


from django.db import models
import json
# from jsonfield import JSONField
# Create your models here.

#订单
class Order(models.Model):
    orderNo = models.CharField(primary_key=True, max_length=7) #订单编号，由日期和三位编号组成，如0402005
    # user = models.FreignKey(User) #用户信息
    allup = models.TextField() #总的水果数量，把各种水果的量和价格构建成json对象，如：{“apple":{"price":"2.5","amount":"3","measurement":"0"},"banana":....}
    #price-单价；amount-数量；measurement-称量方式，1-以“个”算，0-以“斤”算
    allmoney = models.FloatField(null=True) #总金额
    delivery = models.BooleanField(default=True) #配送方式，true-自取，false-送到宿舍
    state = models.BooleanField(default=False) #状态，true-已经配送，false-还没配送
    phone = models.CharField(max_length=11) #手机号码
    dorm = models.CharField(max_length=4) #宿舍号
    remarks = models.TextField(blank=True) #备注
    time = models.DateTimeField(auto_now=True, auto_now_add=False) #生成订单的时间
    class Meta:
        ordering=['time']

#水果价格
class Fruit(models.Model):
    fruitType = models.PositiveSmallIntegerField(primary_key=True) #水果类型，1-苹果，2-香蕉，3-雪梨，4-柠檬
    fruitName = models.CharField(max_length=50) #水果类型
    price = models.FloatField() #水果单价
    measurement = models.BooleanField(default=True) #measurement-称量方式，true-以“个”算，false-以“斤”算
    commentSum = models.IntegerField() #评论总数
    amount = models.IntegerField() #总售量
    picture = models.URLField() #图片

#用户信息
# class User(models.Model):
#     userId = models.CharField(max_length=10, primary_key=True) #用户ID
#     username = models.CharField(max_length=20) #用户名
#     contact = models.CharField(max_length=11) #联系方式
#     qqNum = models.CharField(max_length=15, blank=True) #qq号码
#     password = models.CharField(max_length=30) #密码

#评论
class Comment(models.Model):
    # user = models.ForeignKey(User) #用户
    # order = models.ForeignKey(Order) #订单
    fruit = models.ForeignKey(Fruit) #水果
    comment = models.TextField() #评论
    time = models.DateTimeField(auto_now=True, auto_now_add=False) #评论时间
    class Meta:
        ordering=['-time']

    def formatTime(self):
        return self.time.strftime('%Y-%m-%d %H:%M:%S')

# class JSONField(models.TextField):
#     __metaclass__ = models.SubfieldBase
#     description = "Json"
#     def to_python(self, value):
#         v = models.TextField.to_python(self, value)
#         try:
#             return json.loads(v)['v']
#         except:
#             pass
#         return v
#     def get_prep_value(self, value):
#         return json.dumps({'v':value})
