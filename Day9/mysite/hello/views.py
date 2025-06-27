from django.shortcuts import rend
from django.http import HttpResponse

def home (request):
 return HttpResponse("Hello,Django!")
