# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0004_auto_20151119_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MMR', models.CharField(max_length=100)),
                ('hero', models.CharField(max_length=500)),
                ('rank', models.IntegerField(default=0)),
                ('server', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=5)),
                ('hour_rate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='em',
            new_name='email',
        ),
        migrations.AddField(
            model_name='coach',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
    ]
