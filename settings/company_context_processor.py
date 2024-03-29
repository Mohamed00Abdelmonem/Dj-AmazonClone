from .models import Company
from accounts.models import Profile, Phone, Address
# from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def get_company_data(request):
    data = Company.objects.last()
    return {'company_data':data}



# @login_required
# def get_user_data(request):
#     user_profile = Profile.objects.get(user=request.user)
#     return {'user_data': user_profile}




def get_user_data(request):
    # Make sure the user is authenticated
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)
        user_phone = Phone.objects.filter(user=request.user)
        user_address = Address.objects.filter(user=request.user)
        return {'user_data': user_profile, 'user_phone':user_phone, 'user_address':user_address}
    else:
        return {'user_data': None}

