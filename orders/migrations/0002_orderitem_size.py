# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default='S', max_length=20),
        ),
    ]