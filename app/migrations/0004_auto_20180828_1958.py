# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-28 19:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_base_campania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campania',
            name='fecha_cargada',
            field=models.DateTimeField(db_column='fecha cargada', default=datetime.datetime(2018, 8, 28, 19, 58, 57, 903980)),
        ),
    ]
