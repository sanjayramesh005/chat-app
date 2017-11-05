# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_resume_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInternships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScholasticAchievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.TextField()),
                ('verified', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='academic_details',
            new_name='AcademicDetails',
        ),
        migrations.RemoveField(
            model_name='project_internships',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='scholastic_achievements',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='technical_skill',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='academic_detail',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='academics',
        ),
        migrations.AddField(
            model_name='exam',
            name='resume',
            field=models.ForeignKey(default=1, to='first.Resume'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='project_internships',
        ),
        migrations.DeleteModel(
            name='scholastic_achievements',
        ),
        migrations.DeleteModel(
            name='technical_skill',
        ),
        migrations.AddField(
            model_name='technicalskill',
            name='resume',
            field=models.ForeignKey(to='first.Resume'),
        ),
        migrations.AddField(
            model_name='scholasticachievements',
            name='resume',
            field=models.ForeignKey(to='first.Resume'),
        ),
        migrations.AddField(
            model_name='projectinternships',
            name='resume',
            field=models.ForeignKey(to='first.Resume'),
        ),
    ]
