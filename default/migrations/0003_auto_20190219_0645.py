# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-02-19 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20190215_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='purchase_quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='injection',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
