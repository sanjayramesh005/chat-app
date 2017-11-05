# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20161026_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='proof',
            field=models.FileField(null=True, upload_to=b'exams'),
        ),
        migrations.AddField(
            model_name='projectinternships',
            name='proof',
            field=models.FileField(null=True, upload_to=b'projectinternships'),
        ),
        migrations.AddField(
            model_name='resume',
            name='CPI',
            field=models.FloatField(default=10, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scholasticachievements',
            name='proof',
            field=models.FileField(null=True, upload_to=b'exams'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='cgpa_percentage',
            field=models.FloatField(verbose_name=b'CGPA/Percentage'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Exam Name'),
        ),
        migrations.AlterField(
            model_name='scholasticachievements',
            name='string',
            field=models.TextField(verbose_name=b'Achievement'),
        ),
    ]
