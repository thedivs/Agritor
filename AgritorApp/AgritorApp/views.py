# Created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

    # return HttpResponse("Hello World !")


def about(request):
    return HttpResponse("This is about Page")
