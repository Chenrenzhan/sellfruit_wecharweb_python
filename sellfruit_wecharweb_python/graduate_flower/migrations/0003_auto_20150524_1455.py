# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graduate_flower', '0002_flower_floweraorder_flowerpicture_order_flower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowerpicture',
            name='picture_presentation',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
