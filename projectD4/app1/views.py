from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vishnu(request):
    return render(request,'vishnu.html')

