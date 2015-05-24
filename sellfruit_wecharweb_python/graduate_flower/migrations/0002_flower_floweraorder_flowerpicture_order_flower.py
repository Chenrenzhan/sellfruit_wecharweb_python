# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduate_flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flower_name', models.CharField(max_length=50)),
                ('flower_presentation', models.TextField(default=b'', blank=True)),
                ('flower_price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FloweraOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('totalamount', models.FloatField(default=0.0)),
                ('gtime', models.DateTimeField()),
                ('phone', models.CharField(max_length=11)),
                ('remarks', models.TextField(blank=True)),
                ('has_delivery', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlowerPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture_url', models.CharField(max_length=150)),
                ('picture_name', models.CharField(max_length=50)),
                ('picture_presentation', models.TextField(default=b'')),
                ('flower', models.ForeignKey(to='graduate_flower.Flower')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_Flower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flower', models.ForeignKey(to='graduate_flower.Flower')),
                ('flower_order', models.ForeignKey(to='graduate_flower.FloweraOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
