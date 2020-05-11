from django.shortcuts import render
from allauth.account.views import LoginView, SignupView, PasswordResetView
from django.views.decorators.csrf import csrf_protect
from allauth.account.forms import ResetPasswordForm

class LogIn(LoginView):
    template_name = "login.html"

class SignUp(SignupView):
    template_name = "signup.html"


class Reset(PasswordResetView):
    template_name = 'recover.html'
    def save(self):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save()

        # Add your own processing here.

        # Ensure you return the original result
        return email_address