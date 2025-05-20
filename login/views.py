from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')

    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                error = 'Username atau password salah.'
    else:
        form = LoginForm()
    return render(request, 'login_app/login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('login:login')