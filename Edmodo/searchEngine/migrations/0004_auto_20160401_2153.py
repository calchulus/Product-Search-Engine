# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0003_auto_20160401_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_info',
            old_name='_id',
            new_name='product_id',
        ),
    ]
