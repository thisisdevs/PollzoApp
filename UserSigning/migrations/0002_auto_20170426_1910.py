# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSigning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(upload_to='profile_pic/'),
        ),
    ]
