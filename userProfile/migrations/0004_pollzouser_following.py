# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_pollzouser_desciption'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollzouser',
            name='following',
            field=models.ManyToManyField(related_name='_pollzouser_following_+', to='userProfile.PollzoUser'),
        ),
    ]
