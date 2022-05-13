# Generated by Django 2.0.5 on 2018-06-01 05:08

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('a0b8f7f2-cd7f-4a8b-8b4b-7f9fde3edf71'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('TODO', 'To Do'), ('DONE', 'Done'), ('TEST', 'In Testing'), ('PROG', 'In Progress')], max_length=4)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2018, 5, 31, 23, 8, 55, 205898))),
                ('date_modified', models.DateTimeField(default=datetime.datetime(2018, 5, 31, 23, 8, 55, 205898))),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
