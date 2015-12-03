# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server', models.CharField(max_length=50)),
                ('champion', models.CharField(max_length=500)),
                ('role', models.CharField(max_length=500)),
                ('pricerate', models.FloatField(default=0.0)),
                ('avatar', models.ImageField(upload_to=b'')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('pricerate', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField()),
                ('date', models.DateTimeField()),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='reviewing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField()),
                ('date', models.DateTimeField()),
                ('rating', models.IntegerField(default=0)),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_stars', models.PositiveIntegerField(null=True)),
                ('communication_stars', models.PositiveIntegerField(null=True)),
                ('helpfulness_stars', models.PositiveIntegerField(null=True)),
                ('comment', models.CharField(max_length=300, null=True)),
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
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('MMR', models.IntegerField(default=0)),
                ('skype', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='coach',
            field=models.ForeignKey(to='sideapp.Signup'),
        ),
        migrations.AddField(
            model_name='reviewing',
            name='student',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='report',
            name='student',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='coaching',
            name='student',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='coach',
            name='username',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='usr',
            field=models.ForeignKey(to='sideapp.User'),
        ),
    ]
