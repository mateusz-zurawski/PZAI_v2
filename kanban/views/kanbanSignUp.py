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

class KanbanSignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/sign_up.html"

def signup(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        print("POOOOOOOOOOOOOOOOOOOSSSSSSSSSSSSSSSSSTTTTTTTTTTTT")
        # if form.is_valid():  
        # save form in the memory not in database  
        user = form.save(commit=False)  
        user.is_active = False  
        # user.save()  
        # to get the domain of the current site  
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        to_email = form.cleaned_data.get('email')
        mail_subject = "Link"
        message = "test"
        send_message = EmailMessage(mail_subject, message, to=[to_email])
        send_message.content_subtype = "html"
        send_message.send()
        # message = "Test msql"
        # # render_to_string('registration/login.html', {  
        # #     'user': user,  
        # #     'domain': current_site.domain,  
        # #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
        # #     'token': '1234567890'#account_activation_token.make_token(user),  
        # # })  
        # to_email = form.cleaned_data.get('email')  
        # email = EmailMessage(  
        #             mail_subject, message, to=[to_email]  
        # )  
        # email.send()  
        print('end')
        val = send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['matzur2020@gmail.com'],
            fail_silently=False,
        )
        print(val)
        return HttpResponse('Please confirm your email address to complete the registration')  
    else:  
        return KanbanSignUp.as_view()
 