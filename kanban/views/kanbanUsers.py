from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# from django.contrib.auth.forms import UserCreationForm
from kanban.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail

from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
# from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.auth.models import User,Group
from . import Index

class KanbanUsers(Index):
    template_name = "kanban/users.html"
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        # model = User
        fields = '__all__'
        users = User.objects.all()
        groups = Group.objects.all()

        success_url = reverse_lazy("index")
        context['users'] = User.objects.all()
        context['groups'] = Group.objects.all()
        return context