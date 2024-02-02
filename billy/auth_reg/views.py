from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *

# Create your views here.

def reg(request):
        return render(request, 'auth_reg/reg.html') 


def auth(request):
        return render(request, "auth_reg/auth.html")


def registrations(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                confirm_password = request.POST.get('repPassword')
                if password == confirm_password:
                        user = User.objects.create_user(username=username, password=password)
                        user_profile = UserProfile(user=user)
                        user_profile.save()
                        return JsonResponse({'username': username})
        return JsonResponse({'error': 'Invalid request method shakal'})
        
def autho(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username = username, password = password)
                if user is not None:
                        login(request, user)
                else:
                        print('Didi')

        return JsonResponse({'error': 'Invalid request method'})
