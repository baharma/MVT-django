from django.shortcuts import render,redirect
from .forms import bukuForm
# Create your views here.

def index(request):
    data = "Haiya"
    return render(request, 'page/buku.html', {'data': data})


def createTodoView(request):
    form = bukuForm
    if request.bukuForm == "POST":
        form = bukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todoapp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)