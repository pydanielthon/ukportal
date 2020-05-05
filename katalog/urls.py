from django.urls import path
from . import views
app_name = 'katalog'
urlpatterns = [
    path('katalog/', views.katalog_list, name='katalog_list'),
    path('dodajfirme/', views.dodajfirme, name='dodajfirme'),
    path('kategoria/<int:pk>/', views.kategoria, name='kategoria'),

    path('firma/<int:pk>/', views.firma_detail, name='firma_detail'),
]