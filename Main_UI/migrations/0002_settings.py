# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_UI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clef', models.CharField(max_length=100)),
                ('valeur', models.CharField(max_length=200)),
            ],
        ),
    ]