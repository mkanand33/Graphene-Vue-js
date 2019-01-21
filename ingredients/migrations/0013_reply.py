# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-10 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ingredients', '0012_auto_20190107_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Blog')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Comment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
