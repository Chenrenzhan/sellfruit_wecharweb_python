#!/usr/bin/python
#encoding=utf-8

from django.db import models

# Create your models here.



"""花的订单类"""
class FloweraOrder(models.Model):
    #订单总金额
    totalamount = models.FloatField(default=0.00)

    #订单生产时间
    gtime = models.DateTimeField(auto_now=False, auto_now_add=False)
    #电话
    phone = models.CharField(max_length=11)
    #备注
    remarks = models.TextField(blank=True)
    #是否已配送, False-未配送, True-已配送
    has_delivery = models.BooleanField(default=False)

"""花的信息类"""
class Flower(models.Model):
    #花的名字
    flower_name = models.CharField(max_length=50)
    #花的描述
    flower_presentation = models.TextField(blank=True, default='')
    #花的价格
    flower_price = models.FloatField()

    def get_picture(self):
        try:
            picture = FlowerPicture.objects.get(flower = self)
            return picture
        except Exception as e:
            print(e)
            return None



"""花的图片"""
class FlowerPicture(models.Model):
    flower = models.ForeignKey(Flower)
    #花的图片的地址
    picture_url = models.CharField(max_length=150)
    #图片的名字
    picture_name = models.CharField(max_length=50)
    #图片描述
    picture_presentation = models.TextField(blank=True, default='')


"""订单中包含的花的关系类"""
class Order_Flower(models.Model):
    flower_order = models.ForeignKey(FloweraOrder)
    flower = models.ForeignKey(Flower)
    #取花时间,0-26号,1-29号,2-30号
    take_time = models.SmallIntegerField(default=0)

    @classmethod
    def get_flower_list(cls, order):
        try:
            return cls.objects.filter(flowe_order = order)
        except Exception as e:
            print(e)
            return None
