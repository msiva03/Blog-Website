from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return (HttpResponseRedirect('/post/home/'))
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                homeurl = reverse('home')
                return HttpResponseRedirect(homeurl)
        else:
            form = RegisterForm()        
        return render(request, 'accounts/register.html', {'form': form})

def auth_login(request):
    if request.user.is_authenticated:
        return (HttpResponseRedirect('/post/home/'))
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data= request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username = username, password = password)
                print(user)
                if user is not None:
                    login(request, user)
                    homeurl = reverse('home')
                    return HttpResponseRedirect(homeurl)
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})