import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_mig5'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('No Author', 'No Author'), ('test', 'test'), ('test2', 'test2'), ('test5', 'test5'), ('test3', 'test3'), ('test1', 'test1'), ('test4', 'test4')], default='No_Author', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 22, 12, 46, 16517)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 22, 12, 46, 16517)),
        ),
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.CharField(choices=[('group1', 'group1'), ('all', 'all'), ('group3', 'group3'), ('group2', 'group2')], default='ALL', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('PROG', 'In Progress'), ('TEST', 'In Testing'), ('DONE', 'Done'), ('TODO', 'To Do')], default='TODO', max_length=4),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 22, 12, 46, 26013)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 22, 12, 46, 26013)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4b76bf6b-8815-4876-85c8-697f0680340b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
