from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse

from django.views import View
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import generic

# class KanbanSignUp(UserCreationForm):
#     template_name = 'registration/sign_up.html'
#     extra_context = {'next': reverse_lazy('index')}

# class KanbanSignUp(View):
#     def get(self, request):
#         return render(request, 'registration/sign_up.html', { 'form': UserCreationForm() })

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(reverse('login'))

#         return render(request, 'registration/sign_up.html', { 'form': form })



class KanbanSignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/sign_up.html"