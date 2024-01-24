from .models import Company
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



def get_company_data(request):
    data = Company.objects.last()
    return {'company_data':data}



@login_required
def get_user_data(request):
    user_profile = Profile.objects.get(user=request.user)
    return {'user_data': user_profile}