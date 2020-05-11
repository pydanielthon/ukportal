from django.urls import path
from .views import LogIn, SignUp, Reset
app_name = 'authentications'

urlpatterns = [
    path('logowanie/', LogIn.as_view(), name='login'),
    path('rejestracja/', SignUp.as_view(), name='signup'),
    path('reset/', Reset.as_view(), name='account_reset_password'),

]