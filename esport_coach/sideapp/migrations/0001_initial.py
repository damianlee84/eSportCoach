# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MMR', models.IntegerField(default=0)),
                ('hero', models.CharField(max_length=500)),
                ('rank', models.IntegerField(default=0)),
                ('server', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=5)),
                ('hour_rate', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='register',
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
            name='Tutee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tutee',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='coach',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='admin',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
    ]
