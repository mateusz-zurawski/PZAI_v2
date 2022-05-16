from django.views.generic import  TemplateView

from ..models import Task

class Index(TemplateView):
    template_name = 'kanban/index.html'


    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        groups = []
        for group in self.request.user.groups.all():
            print(group.name)
            groups.append(group.name)
        print(groups)

        todo_tasks = Task.objects.filter(status='TODO', group__in=groups)
        prog_tasks = Task.objects.filter(status='PROG', group__in=groups)
        test_tasks = Task.objects.filter(status='TEST', group__in=groups)
        done_tasks = Task.objects.filter(status='DONE', group__in=groups)



        context['TODO_list'] = todo_tasks.order_by('-priority')[:15]
        context['PROG_list'] = prog_tasks.order_by('-priority')[:15]
        context['TEST_list'] = test_tasks.order_by('-priority')[:15]
        context['DONE_list'] = done_tasks.order_by('-priority')[:15]

        return context

