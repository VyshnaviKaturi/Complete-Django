from django.shortcuts import render

# Create your views here.
def jinjaPrint(request):
    d={'name':'Vyshu','age':16,'song':'jingidi jingidi'}
    return render(request,'jinjaPrint.html',d)
