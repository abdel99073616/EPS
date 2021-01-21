from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
from .form import CreateUserForm

# Create your views here.

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.info(request , 'Username Or Password is invalid')
    context = {}
    return render(request , 'login.html' , context)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           return redirect('login')
    context = {'form':form}
    return render(request , 'register.html', context)


def Home(request):
    return render(request,'index.html')
