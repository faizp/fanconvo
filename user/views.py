from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib import messages
from django.http import JsonResponse

import pytz


def index(request):
    return render(request, 'user/sign-up.html', {'timezones': pytz.common_timezones})


# fan account sign up method
def fan_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['fanFirstname']
        last_name = request.POST['fanLastname']
        username = request.POST['fanUsername']
        if User.objects.filter(username = username).exists():
            return JsonResponse('false', safe=False)
        email = request.POST['fanEmail']
        timezone = request.POST['fanTimezone']
        password = request.POST['fanPassword']
        print(first_name, last_name, username, email, timezone, password)
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        Profile.objects.create(user=user, timezone=timezone, is_talent=False)
        return JsonResponse('true', safe=False)


# talent account signup method 
def talent_sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['talentFirstname']
        last_name = request.POST['talentLastname']
        username = request.POST['talentUsername']
        if User.objects.filter(username = username).exists():
            return JsonResponse('false', safe=False)
        email = request.POST['talentEmail']
        timezone = request.POST['talentTimezone']
        password = request.POST['talentPassword']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        Profile.objects.create(user=user, timezone=timezone, is_talent=True)
        return JsonResponse('true', safe=False)
     