# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190409_2146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Neighborhood',
            new_name='Village',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='neighborhood',
            new_name='village',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='neighborhood',
            new_name='village',
        ),
        migrations.RenameField(
            model_name='police',
            old_name='neighborhood',
            new_name='village',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='neighborhood',
            new_name='village',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='neighborhood',
            new_name='village',
        ),
    ]