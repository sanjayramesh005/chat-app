# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20161107_0939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicDetails',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='projectinternships',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='user',
        ),
        migrations.RemoveField(
            model_name='scholasticachievements',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='technicalskill',
            name='resume',
        ),
        migrations.DeleteModel(
            name='exam',
        ),
        migrations.DeleteModel(
            name='ProjectInternships',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='ScholasticAchievements',
        ),
        migrations.DeleteModel(
            name='TechnicalSkill',
        ),
    ]
