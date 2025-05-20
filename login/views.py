from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        username_or_email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            error = "Username/email atau password salah."

    return render(request, 'login_app/login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('login:login')