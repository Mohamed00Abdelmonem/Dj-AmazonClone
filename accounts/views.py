from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SignupForm, ActivationForm
from django.contrib.auth.models import User
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['password']
            form.save

            profile = Profile.objects.get(user__username= username)

            send_mail(
                "Activate Your Acount",
                f"Welcome {username} \n use this code {profile.code} to activate you account.",
                "mmohamedabdelm@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect('/accounts/{username}/activate')

    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form':form})        



def activate(request, username):
    pass




def profile(request):
    pass