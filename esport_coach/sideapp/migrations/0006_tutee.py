# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0005_auto_20151119_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.ForeignKey(to='sideapp.User')),
            ],
        ),
    ]
