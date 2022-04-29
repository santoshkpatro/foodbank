from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def login_view(request):
    return render(request, 'accounts/login.html')