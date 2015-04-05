# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellfruit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['time']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
