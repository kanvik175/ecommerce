# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180813_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]
