# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'Name')),
                ('public', models.BooleanField(default=False, verbose_name=b'Public')),
                ('code', models.TextField(verbose_name=b'Code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Last edit at')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(to='web.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=15, verbose_name=b'Name')),
            ],
        ),
        migrations.AddField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(to='web.Tag'),
        ),
    ]
