# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='result_id',
            field=models.CharField(default=b'', max_length=60),
            preserve_default=True,
        ),
    ]
