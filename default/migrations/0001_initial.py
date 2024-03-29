# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-02-09 17:26
from __future__ import unicode_literals

import default.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Injection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to=default.models.user_directory_path_injections)),
                ('brand', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('composition', models.TextField(null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('pharmaceutical_name', models.TextField(null=True)),
                ('unit_name', models.CharField(max_length=200, null=True)),
                ('price_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_25', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_50', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_100', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to=default.models.user_directory_path_medicines)),
                ('brand', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('composition', models.TextField(null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('pharmaceutical_name', models.TextField(null=True)),
                ('unit_name', models.CharField(max_length=200, null=True)),
                ('price_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_25', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_50', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_100', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to=default.models.user_directory_path_tablets)),
                ('brand', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('composition', models.TextField(null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('pharmaceutical_name', models.TextField(null=True)),
                ('unit_name', models.CharField(max_length=200, null=True)),
                ('price_1', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_25', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_50', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_100', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
