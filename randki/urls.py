from django.urls import path
from . import views

app_name = 'randki'

urlpatterns = [
    path('glowna/', views.glowna, name='glowna'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('kategoria/<int:pk>/', views.kategoria, name='kategoria'),
    path('dodaj/', views.dodaj, name='dodaj'),

]