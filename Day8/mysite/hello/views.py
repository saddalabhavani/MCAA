from django.shortcuts import r
from django.http import HttpResponse


# Create your views here.
def  home(request):
    return HttpResponse("day1")
