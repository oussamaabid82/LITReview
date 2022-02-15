from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from . import forms


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                                username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password'],
                                )
            if user is not None:
                login(request, user)
                return redirect('blog')
            else:
                message = 'Identifiants invalides.'
                return render(request, 'client/login.html', context={'form': form, 'message': message})
                
    return render(request, 'client/login.html', context={'form': form})

def logout_user(request):
      logout(request)
      return redirect('login') 
     
def registration_page(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
                        # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'client/form.html', context={'form': form})