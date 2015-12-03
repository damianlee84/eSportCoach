# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0007_remove_ratings_num_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_stars', models.PositiveIntegerField(null=True)),
                ('communication_stars', models.PositiveIntegerField(null=True)),
                ('helpfulness_stars', models.PositiveIntegerField(null=True)),
                ('comment', models.CharField(max_length=300, null=True)),
                ('coach', models.ForeignKey(to='sideapp.Signup')),
            ],
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='coach',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
