# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-11 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0004_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='text',
            new_name='content',
        ),
    ]
