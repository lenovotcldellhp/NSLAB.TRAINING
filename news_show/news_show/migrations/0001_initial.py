# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField()),
                ('title', models.TextField()),
                ('info', models.TextField()),
                ('imgsrc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('num', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
