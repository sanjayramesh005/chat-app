# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2017, 11, 5, 22, 0, 55, 556071))),
                ('text', models.TextField()),
                ('from_user', models.ForeignKey(related_name='fromuser', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
