# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nuser', '0004_auto_20160617_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoundPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('location', models.CharField(max_length=40, blank=True)),
                ('icture', models.ImageField(upload_to=b'pictures')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 24, 19, 23, 30, 59139, tzinfo=utc)),
        ),
    ]
