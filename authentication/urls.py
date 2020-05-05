from django.urls import path
from .views import LogIn, SignUp
app_name = 'authentications'

urlpatterns = [
    path('logowanie/', LogIn.as_view(), name='login'),
    path('rejestracja/', SignUp.as_view(), name='signup'),

]