# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0003_auto_20151116_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=100)),
                ('em', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='pricerate',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='reputation',
            field=models.PositiveIntegerField(),
        ),
    ]
