# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('manual', models.FileField(blank=True, null=True, upload_to='')),
                ('driver', models.FileField(blank=True, null=True, upload_to='')),
                ('specifications', models.TextField()),
                ('completeness', models.TextField()),
            ],
        ),
    ]