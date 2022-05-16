from tokenize import group
from . import Index
from django.contrib.postgres.search import SearchVector
from ..models import Task


class AllTasksGroup(Index):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("--------------------------------------")

        group = kwargs['group']
        if group == 'all':
            groups = []
            for group in self.request.user.groups.all():
                print(group.name)
                groups.append(group.name)
            print(groups)
            todo_tasks = Task.objects.filter(status='TODO', group__in=groups)
            prog_tasks = Task.objects.filter(status='PROG', group__in=groups)
            test_tasks = Task.objects.filter(status='TEST', group__in=groups)
            done_tasks = Task.objects.filter(status='DONE', group__in=groups)

        else :
            todo_tasks = Task.objects.filter(status='TODO', group=group)
            prog_tasks = Task.objects.filter(status='PROG', group=group)
            test_tasks = Task.objects.filter(status='TEST', group=group)
            done_tasks = Task.objects.filter(status='DONE', group=group)

        context['TODO_list'] = todo_tasks.order_by('-priority')[:15]
        context['PROG_list'] = prog_tasks.order_by('-priority')[:15]
        context['TEST_list'] = test_tasks.order_by('-priority')[:15]
        context['DONE_list'] = done_tasks.order_by('-priority')[:15]

        return context

