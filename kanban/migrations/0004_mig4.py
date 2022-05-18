import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0003_mig3'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 18, 1, 38, 518632)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 18, 1, 38, 518632)),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('PROG', 'In Progress'), ('DONE', 'Done'), ('TEST', 'In Testing')], default='TODO', max_length=4),
        ),
        migrations.AlterField(
            model_name='task',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 18, 1, 38, 519633)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 18, 1, 38, 519633)),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('cefbda30-2aba-4917-b86d-a359affd9c0c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
