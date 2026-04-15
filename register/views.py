from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import authenticate


# Create your views here.
def register(request):
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
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})