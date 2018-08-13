# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180813_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
