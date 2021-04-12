from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse("<h1>Hello world</h1>")

def view2(request,email):
    return render(request,"view2.html",context={'email':email,'name':"Akshay"})

def view3(request,name):
    return HttpResponse(f'<h1>Hello Mr./Ms. {name}</h1>')