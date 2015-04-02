# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fruitType', models.PositiveSmallIntegerField()),
                ('commment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderNo', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('allup', models.TextField()),
                ('allmoney', models.IntegerField(null=True)),
                ('delivery', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('fruitType', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
