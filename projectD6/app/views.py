from django.shortcuts import render

# Create your views here.
def conditional(request):
    d = {'name': 'Afrin', 'age':17}
    return render(request,'conditional.html',d)
def conditional2(request):
    d1={'name':'Chukki', 'age':20}
    return render(request,'conditional2.html',d1)