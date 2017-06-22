# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 19:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='discussion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discussions.Discussion'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discussions.Comment'),
        ),
        migrations.AlterField(
            model_name='subcomment',
            name='commenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
