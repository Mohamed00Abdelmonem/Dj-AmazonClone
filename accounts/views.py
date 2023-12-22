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
            email = form.cleaned_data['email']

            user = form.save(commit=False)
            user.is_active = False
            user.save()  

            profile = Profile.objects.get(user__username=username)

            send_mail(
                "Activate Your Account",
                f"Welcome {username} \n use this code {profile.code} to activate your account.",
                "mmohamedabdelm@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})



def activate(request, username):
    profile = Profile.objects.get(user__username= username)
    if request.method == "POST":
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code=''
                profile.save()


                user = User.objects.get(user=profile.user)
                user.is_active = True
                user.save() 

                return redirect('/accounts/login')
    else: 
        form = ActivationForm()        
    return render(request,'registration/activate.html', {'form':form})        





def profile(request):
    pass