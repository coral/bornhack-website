# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160515_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
