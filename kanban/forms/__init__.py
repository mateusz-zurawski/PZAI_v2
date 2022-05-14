from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False
        print("save")

        if commit:
            user.save()
            send_mail(
                        'Link to activate the account',
                        'Link : http://127.0.0.1:8000/accounts/activate/'+str(user.id),
                        'from@example.com',
                        [self.cleaned_data["email"]],
                        fail_silently=False,
                    )


            print("commit")
            pass
        return user