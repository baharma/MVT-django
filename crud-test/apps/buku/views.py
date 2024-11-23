from django.shortcuts import render

# Create your views here.

def index(request):
    data = "Haiya"
    return render(request, 'layout/base.html', {'data': data})
