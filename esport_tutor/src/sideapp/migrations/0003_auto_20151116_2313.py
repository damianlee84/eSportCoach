# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0002_auto_20151116_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='hero',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 15, 313091, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='mmr',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 28, 957152, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='pricerate',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 38, 588999, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='rating',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 44, 61125, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='reputation',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 50, 597350, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='server',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 12, 58, 477469, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='students',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 23, 13, 4, 165379, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
