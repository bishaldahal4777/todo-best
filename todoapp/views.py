from django.shortcuts import render,HttpResponse
from .import RegisterForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def register_view(request):
    form = RegisterForm()
    context ={
        'form':form
    }
    return render(request, "register.html")

def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    return HttpResponse("Logout")

def delete_task(request, id):
    return HttpResponse("Deleted")