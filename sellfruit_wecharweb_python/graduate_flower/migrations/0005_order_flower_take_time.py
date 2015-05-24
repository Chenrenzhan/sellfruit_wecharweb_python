# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduate_flower', '0004_auto_20150524_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_flower',
            name='take_time',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
