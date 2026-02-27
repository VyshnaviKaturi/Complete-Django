from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vyshu(request):
    return HttpResponse('I love vyshu')