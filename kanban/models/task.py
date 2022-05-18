import datetime
from tokenize import group
import uuid
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import Group

class Task(models.Model):
    class Meta:
        ordering = ['-date_modified']

    STATUS_CHOICES = {
        ('TODO', 'To Do'),
        ('PROG', 'In Progress'),
        ('TEST', 'In Testing'),
        ('DONE', 'Done'),
    }

    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    priority = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='TODO')

    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_modified = models.DateTimeField(default=datetime.datetime.now())

    
    
    User = get_user_model()
    users = User.objects.all()
    print(users)

    usrs = {
        ('TODO', 'To Do'),
        ('PROG', 'In Progress'),
        ('TEST', 'In Testing'),
        ('DONE', 'Done'),
    }
    users_toulpe = {('No Author','No Author')}


    for user in users:
        print (user.username)
        users_toulpe.add((user.username,user.username))
    print(users_toulpe)

    groups_toulpe = {('default','default')}
    groups = Group.objects.all()

    for group in groups:
        print(group.name)
        groups_toulpe.add((group.name,group.name))
    print(groups_toulpe)

    author = models.CharField(max_length=200, choices =users_toulpe, default='No_Author')
    group = models.CharField(max_length=200, choices =groups_toulpe, default='default')
    archive = models.BooleanField(default=False)

    
    def __str__(self):
        return '{title}'.format(title=self.title)

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.uuid})

    def increase_status(self) -> None:
        if self.status == 'TODO':
            self.status = 'PROG'
        elif self.status == 'PROG':
            self.status = 'TEST'
        elif self.status == 'TEST':
            self.status = 'DONE'

        self.save()

    def decrease_status(self) -> None:
        if self.status == 'PROG':
            self.status = 'TODO'
        elif self.status == 'TEST':
            self.status = 'PROG'
        elif self.status == 'DONE':
            self.status = 'TEST'

        self.save()

    def max_priority(self) -> None:
        cur_max_priority = Task.objects.all().aggregate(models.Max('priority'))['priority__max']

        self.priority = cur_max_priority + 1
        self.save()

    def min_priority(self) -> None:

        cur_min_priority = Task.objects.all().aggregate(models.Min('priority'))['priority__min']

        self.priority = cur_min_priority - 1
        self.save()