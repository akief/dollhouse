# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseitself', '0002_auto_20150928_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='article',
            name='location',
        ),
        migrations.RemoveField(
            model_name='location',
            name='part',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doll',
            name='image',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doll',
            name='location',
            field=models.ForeignKey(default=0, to='houseitself.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
