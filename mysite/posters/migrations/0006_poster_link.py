# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0005_auto_20170924_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
