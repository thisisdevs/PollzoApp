# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0009_remove_pollzouser_cover_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoverPhoto',
        ),
    ]