# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_clone', '0002_auto_20170717_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
