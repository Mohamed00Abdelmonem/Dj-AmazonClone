from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import SignupForm, ActivationForm
from django.contrib.auth.models import User
from .models import Profile
from product.models import Product, Brand, Review
from orders.models import Order
from django.conf import settings    




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
                settings.EMAIL_HOST_USER,
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
              


                user = User.objects.get(username=profile.user.username)
                user.is_active = True
                user.save() 
                profile.save()
                return redirect('/accounts/login')
    else: 
        form = ActivationForm()        
    return render(request,'registration/activate.html', {'form':form})        




def dashboard(request):
    users = User.objects.all().count()
    products = Product.objects.all().count()
    reviews = Review.objects.all().count()
    brand = Brand.objects.all().count()
    orders = Order.objects.all().count()
    
    return render(request, 'accounts/dashboard.html',{
        'users':users,
        'products':products,
        'reviews':reviews,
        'brand':brand,
        'orders':orders,
    })