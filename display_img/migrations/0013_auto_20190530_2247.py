# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display_img', '0012_auto_20190530_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output_av',
            name='origin_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='display_img.Eyeimg', verbose_name='原图'),
        ),
        migrations.AlterField(
            model_name='output_vessel',
            name='origin_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='display_img.Eyeimg', verbose_name='原图'),
        ),
    ]