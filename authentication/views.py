from django.shortcuts import render
from allauth.account.views import LoginView, SignupView, PasswordResetView
from django.views.decorators.csrf import csrf_protect

class LogIn(LoginView):
    template_name = "login.html"

class SignUp(SignupView):
    template_name = "signup.html"

