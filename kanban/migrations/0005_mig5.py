import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0004_mig4'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.CharField(choices=[('group3', 'group3'), ('all', 'all'), ('group1', 'group1'), ('group2', 'group2')], default='ALL', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.CharField(choices=[('test1', 'test1'), ('No Author', 'No Author'), ('test4', 'test4'), ('test2', 'test2'), ('test3', 'test3'), ('test', 'test'), ('test5', 'test5')], default='No_Author', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 23, 2, 23, 778570)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 23, 2, 23, 778570)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TEST', 'In Testing'), ('PROG', 'In Progress'), ('DONE', 'Done'), ('TODO', 'To Do')], default='TODO', max_length=4),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 23, 2, 23, 790539)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 23, 2, 23, 790539)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2e033afe-80ae-45e3-80a5-bbde39eec14d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
