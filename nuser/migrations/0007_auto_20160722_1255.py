# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nuser', '0006_auto_20160624_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundperson',
            name='uploaded_by',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 12, 55, 13, 768781, tzinfo=utc)),
        ),
    ]
