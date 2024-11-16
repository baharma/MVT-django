from django.shortcuts import render
from django.urls import path
from . import views
from django.http import HttpResponse

def index(request):
    return render(request,'blog.html')


def cari(request):
    return HttpResponse('<h1>data</h1>')
