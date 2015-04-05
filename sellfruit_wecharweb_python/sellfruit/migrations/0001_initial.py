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
                ('comment', models.TextField()),
                ('time', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('fruitType', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('fruitName', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('measurement', models.BooleanField(default=True)),
                ('commentSum', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('picture', models.URLField()),
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
                ('allmoney', models.FloatField(null=True)),
                ('delivery', models.BooleanField(default=True)),
                ('state', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=11)),
                ('dorm', models.CharField(max_length=4)),
                ('remarks', models.TextField(blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='fruit',
            field=models.ForeignKey(to='sellfruit.Fruit'),
            preserve_default=True,
        ),
    ]
