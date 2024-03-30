from .models import Add_To_Favourite


def get_add_to_favourite(request):
    if request.user.is_authenticated:
         favourite = Add_To_Favourite.objects.filter(user=request.user)
    else:
         favourite = 0
    return {'favourite':favourite}