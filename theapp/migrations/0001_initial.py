# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-05-07 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DumDatas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kartid', models.CharField(max_length=200)),
                ('zaman', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
