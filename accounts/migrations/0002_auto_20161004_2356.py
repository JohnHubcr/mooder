# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(blank=True, max_length=64, verbose_name='用户名'),
        ),
    ]
