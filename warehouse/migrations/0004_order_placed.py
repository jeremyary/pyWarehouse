# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='placed',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'order placed'),
            preserve_default=True,
        ),
    ]
