# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mmr', models.CharField(max_length=50)),
                ('server', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField()),
                ('reputation', models.PositiveIntegerField()),
                ('students', models.CharField(max_length=50)),
                ('pricerate', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=32)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sideapp.User')),
                ('MMR', models.IntegerField(default=0)),
                ('hero', models.CharField(max_length=500)),
                ('server', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=0)),
                ('hour_rate', models.FloatField(default=0.0)),
            ],
            bases=('sideapp.user',),
        ),
        migrations.CreateModel(
            name='Tutee',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sideapp.User')),
            ],
            bases=('sideapp.user',),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
    ]
