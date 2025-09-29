from django.shortcuts import render,HttpResponse, redirect
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
@login_required
def home(request):
    return render(request, "index.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html")
    return render(request, "login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def delete_task(request, id):
    return HttpResponse("Deleted")