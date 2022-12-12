from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import LoginForm, RegisterForm


class AuthView(View):
    @staticmethod
    def get(request):
        return render(request, "accounts_app/auth.html", context={
            "login_form": LoginForm(),
            "register_form": RegisterForm(),
            "title": "Авторизация"
        })


class LoginView(View):
    @staticmethod
    def post(request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно вошли в систему !")
            return redirect("index")
        else:
            messages.error(request, form.errors)
            return redirect("auth")


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        messages.success(request, "Вы успешно вышли из системы")
        return redirect("index")


class RegisterView(View):
    @staticmethod
    def post(request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Вы успешно зарегистрировались ! Добро пожаловать, {user.username} !")
            return redirect("index")
        else:
            messages.error(request, form.errors)
            return redirect("auth")
