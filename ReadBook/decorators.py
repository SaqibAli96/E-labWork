from django.http import HttpResponse 
from .models import UserInfo


def author_only(func):
    def wrapper(request,*args,**kwargs):
        if UserInfo.objects.filter(pk = request.user.id,user_type = "Author").exists():
            return func(request,*args,**kwargs)
        else:
            return HttpResponse("You have no permission to access this page")
    return wrapper