from django.http import HttpResponse
from . import django_task_001

def index(request):
    return HttpResponse("Home")


def jango(request,a,b):
    return django_task_001.jango1(a,b)

