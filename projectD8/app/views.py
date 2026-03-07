from django.shortcuts import render

# Create your views here.
fruits = ['apple','banana','cherry']
def loop1(request):
    return render(request,'loop1.html', {'item_list':fruits})