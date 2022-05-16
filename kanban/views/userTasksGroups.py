from tokenize import group
from . import Index
from django.contrib.postgres.search import SearchVector
from ..models import Task


class UserTasksGroups(Index):
    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        print(kwargs['group'])
        group = kwargs['group']
        todo_tasks = Task.objects.filter(status='TODO', author=self.request.user.username,group=group)
        prog_tasks = Task.objects.filter(status='PROG', author=self.request.user.username,group=group)
        test_tasks = Task.objects.filter(status='TEST', author=self.request.user.username,group=group)
        done_tasks = Task.objects.filter(status='DONE', author=self.request.user.username,group=group)

        context['TODO_list'] = todo_tasks.order_by('-priority')[:15]
        context['PROG_list'] = prog_tasks.order_by('-priority')[:15]
        context['TEST_list'] = test_tasks.order_by('-priority')[:15]
        context['DONE_list'] = done_tasks.order_by('-priority')[:15]

        return context

