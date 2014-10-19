# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='workers',
        ),
        migrations.AddField(
            model_name='worker',
            name='classifications',
            field=models.ManyToManyField(to='warehouse.Classification', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worker',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'employment date'),
        ),
    ]
