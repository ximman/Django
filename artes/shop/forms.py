from django.contrib.auth import forms
from django.contrib.auth.models import User
from django import forms as fforms



class RegisterForm(forms.UserCreationForm):
    class meta:
        model=User
        fields=('username', 'password1', 'password2')

class LoginForm(forms.AuthenticationForm):
    class meta:
        model=User,
        fields=('username', 'password')


