# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nuser', '0005_auto_20160624_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundperson',
            name='icture',
        ),
        migrations.AddField(
            model_name='foundperson',
            name='picture',
            field=models.ImageField(default=1, upload_to=b'static/images/products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 24, 20, 10, 39, 7105, tzinfo=utc)),
        ),
    ]
