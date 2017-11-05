# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academic_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
                ('board', models.CharField(max_length=100, blank=True)),
                ('institute', models.CharField(max_length=200)),
                ('cgpa_percentage', models.FloatField()),
                ('verified', models.BooleanField(default=False)),
                ('academic_detail', models.ForeignKey(to='first.academic_details')),
            ],
        ),
        migrations.CreateModel(
            name='project_internships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('dept', models.CharField(max_length=4, choices=[(b'CSE', b'Computer Science and Engineering'), (b'MSE', b'Material Science and Engineering'), (b'CHE', b'Chemical Engineering'), (b'BSBE', b'Biological Sciences and Bio Engineering'), (b'AE', b'Aerospace Engineering')])),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('academics', models.OneToOneField(to='first.academic_details')),
            ],
        ),
        migrations.CreateModel(
            name='scholastic_achievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('string', models.TextField()),
                ('verified', models.BooleanField(default=True)),
                ('resume', models.ForeignKey(to='first.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='technical_skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('resume', models.ForeignKey(to='first.Resume')),
            ],
        ),
        migrations.AddField(
            model_name='project_internships',
            name='resume',
            field=models.ForeignKey(to='first.Resume'),
        ),
    ]
