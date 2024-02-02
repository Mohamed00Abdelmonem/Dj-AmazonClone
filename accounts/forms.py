from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter useranme'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class ActivationForm(forms.Form):
    code = forms.CharField(max_length=8)          
    

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']