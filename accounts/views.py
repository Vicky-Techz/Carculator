from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm


def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form = form.save()
      return HttpResponseRedirect(reverse('login'))
  else:
    form = UserRegistrationForm()

  return render(request, 'accounts/register.html', {'regform':form})
  
def user_login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('home'))
  else:
    form = AuthenticationForm()
    
  return render(request, 'accounts/login.html', {'loginform':form})

def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))