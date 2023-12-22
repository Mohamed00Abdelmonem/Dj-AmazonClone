from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    useranme = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter useranme'
            }
        )
    )
    class Meta:
        model = User
        fields = ['useranme', 'email', 'password1', 'password2']




class ActivationForm(forms.Form):
    code = forms.CharField(max_length=8)          
    