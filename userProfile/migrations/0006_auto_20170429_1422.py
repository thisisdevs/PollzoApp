# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0005_auto_20170429_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollzouser',
            name='following',
            field=models.ManyToManyField(blank=True, to='userProfile.PollzoUser'),
        ),
    ]
