from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

# Create your views here.
def registration(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username
        context['password']  = password
        if username and password:
            if password:
                try:
                    User.objects.create_user(username = username, password = password)
                except IntegrityError:
                    context['error'] = 'Такий користувач вже існує!'
            else:
                context['error'] = 'Паролі не співпадають!'
    return render(request, 'auth_reg/reg.html', context)

def authorization(request):
    context = {}
    if request.user.is_authenticated:
        context['error'] = 'Такий користувач вже існує!'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        context['username'] = username
        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
            else:
                context['error'] = 'Невірний логін або пароль'
        else:
            context['error'] = 'Заповніть всі поля'
    return render(request, 'auth_reg/auth.html', context)