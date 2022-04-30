from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def index(request):
    if request.method == 'POST':
        sic = request.POST['sic']
        password = request.POST['password']
        user = authenticate(request, sic=sic, password=password)
        if user is not None:
            login(request, user)
            return redirect('booking_create')
        else:
            messages.warning(request, 'Invalid credentials')
    return render(request, 'home/index.html')