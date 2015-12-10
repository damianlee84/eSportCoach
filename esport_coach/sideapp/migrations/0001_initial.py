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
            name='Champions',
            fields=[
                ('champion', models.CharField(max_length=100, serialize=False, primary_key=True)),
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
                ('avatar', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('pricerate', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('request', models.TextField(blank=True)),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField()),
                ('date', models.DateTimeField()),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_stars', models.PositiveIntegerField(null=True)),
                ('communication_stars', models.PositiveIntegerField(null=True)),
                ('helpfulness_stars', models.PositiveIntegerField(null=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('coach', models.ForeignKey(to='sideapp.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reviewer', models.CharField(max_length=100, null=True)),
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
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('skype', models.CharField(max_length=50)),
                ('mmr', models.PositiveIntegerField(default=0)),
                ('server', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('reputation', models.PositiveIntegerField(default=0)),
                ('students', models.PositiveIntegerField(default=0)),
                ('pricerate', models.FloatField(default=0.0)),
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
                ('userid', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('pname', models.CharField(max_length=100)),
                ('MMR', models.IntegerField(default=0)),
                ('skypeid', models.CharField(max_length=100)),
                ('twitchid', models.CharField(max_length=100)),
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
            name='userid',
            field=models.ForeignKey(to='sideapp.User'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='userid',
            field=models.ForeignKey(to='sideapp.User'),
        ),
    ]
