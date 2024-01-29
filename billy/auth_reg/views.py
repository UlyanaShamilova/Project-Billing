from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
# Create your views here.

def reg(request):
        context = {}
        # if request.method == 'POST':
        #     name_reg = request.POST.get('name_reg')
        #     password_reg = request.POST.get('password_reg')
        #     rep_password = request.POST.get('rep_password')

        #     context['name_reg'] = name_reg
        #     context['password_reg'] = password_reg
        #     context['rep_password'] = rep_password

        #     if name_reg and password_reg and rep_password:
        #         if len(password_reg) > 0:
        #             if password_reg == rep_password:
        #                 try:
        #                         User.objects.create_user(
        #                             username=name_reg,
        #                             password=password_reg
        #                         )
        #                 except IntegrityError:
        #                     context['error'] = 'Такий користувач вже існує.'
        #                 # pass
        #             else:
        #                 context['error'] = 'Паролі не співпадають'
        #         else:
        #             context['error'] = 'Пароль має бути не меньше 8 символів.'
        #     else:
        #         context['error'] = 'Заповніть всі поля'

        return render(request, 'reg.html', context) 


def auth(request):
        return render(request, "auth.html")