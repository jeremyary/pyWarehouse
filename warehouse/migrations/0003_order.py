# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20141017_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('classifications', models.ManyToManyField(to='warehouse.Classification', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
