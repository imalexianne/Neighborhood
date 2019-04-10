# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-09 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='police',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Neighborhood'),
        ),
    ]