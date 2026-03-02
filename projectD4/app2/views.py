from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Dev(request):
    return render(request,'Dev.html')
