from tokenize import group
from . import Index
from django.contrib.postgres.search import SearchVector
from ..models import Task


class UserTasks(Index):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = []

        for group in self.request.user.groups.all():
            print(group.name)
            groups.append(group.name)
        print(groups)
        todo_tasks = Task.objects.filter(status='TODO', author=self.request.user.username,group__in=groups)
        prog_tasks = Task.objects.filter(status='PROG', author=self.request.user.username,group__in=groups)
        test_tasks = Task.objects.filter(status='TEST', author=self.request.user.username,group__in=groups)
        done_tasks = Task.objects.filter(status='DONE', author=self.request.user.username,group__in=groups)

        context['TODO_list'] = todo_tasks.order_by('-priority')[:15]
        context['PROG_list'] = prog_tasks.order_by('-priority')[:15]
        context['TEST_list'] = test_tasks.order_by('-priority')[:15]
        context['DONE_list'] = done_tasks.order_by('-priority')[:15]

        return context

