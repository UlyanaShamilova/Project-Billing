from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
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
        users = UserProfile.objects.all()
        if request.method == 'POST':
                username = request.POST.get('nameReg')
                password = request.POST.get('passwordReg')
                confirm_password = request.POST.get('repPassword')
                
                user = User.objects.create_user(
                        username = username, 
                        password = password, 
                        confirm_password = confirm_password)

                user_profile = UserProfile(user = user)
                user_profile.save()

                return JsonResponse({"username":username})