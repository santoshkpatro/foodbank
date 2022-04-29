from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def login_view(request):
    if request.method == 'POST':
        sic = request.POST['sic']
        password = request.POST['password']
        user = authenticate(request, sic=sic, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout success')
    return redirect('index')