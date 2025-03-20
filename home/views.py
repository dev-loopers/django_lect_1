from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomeView(request):
    return render(request , "home/index.html")


def AboutView(request):
    # return HttpResponse("This is about page ")
    return render(request , "home/about.html")
