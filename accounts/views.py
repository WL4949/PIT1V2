from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginPage
from django .contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                loginPage(request, user)
                return HttpResponseRedirect(reverse('admin:index'))
            loginPage(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('login')
    return render(request, 'signup.html', {'form':form})