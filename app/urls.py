from django.urls import path
from . import views 

app_name = 'app'

urlpatterns = [
    path('', views.homepage, name="home"),
    path('kup/', views.kup, name='kup'),
    path('konto/', views.profil, name='konto'),
    path('platnosc/', views.platnosc, name='platnosc'),
]