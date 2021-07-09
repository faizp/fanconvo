from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib import messages

import pytz


def index(request):
    return render(request, 'user/sign-up.html', {'timezones': pytz.common_timezones})


def fan_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        if User.objects.filter(username = username).exists():
            messages.error(request, "This Username is already taken")
            return redirect('index')
        email = request.POST.get('email')
        timezone = request.POST.get('timezone')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        Profile.objects.create(user=user, timezone=timezone, is_talent=False)
        return redirect('index')


def talent_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        if User.objects.filter(username = username).exists():
            messages.error(request, "This Username is already taken")
            return redirect('index')
        email = request.POST.get('email')
        timezone = request.POST.get('timezone')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        Profile.objects.create(user=user, timezone=timezone, is_talent=True)
        return redirect('index')
