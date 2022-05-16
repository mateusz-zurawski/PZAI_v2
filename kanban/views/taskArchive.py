from django.urls import reverse
from django.shortcuts import  get_object_or_404
from django.views.generic import RedirectView
from django.views.generic.edit import UpdateView

from ..models import Task

class TaskArchive(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # context = super().get_context_data(**kwargs)

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxXX")
        task_pk = kwargs.get('pk')
        print(task_pk)
        task = get_object_or_404(Task, pk=task_pk)
        task.archive = True
        task.save()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxXX")
        return reverse('index')

class TaskRestore(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # context = super().get_context_data(**kwargs)

        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxXX")
        task_pk = kwargs.get('pk')
        print(task_pk)
        task = get_object_or_404(Task, pk=task_pk)
        task.archive = False
        task.save()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxXX")
        return reverse('index')