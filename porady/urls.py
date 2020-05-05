from django.urls import path
from . import views

app_name='porady'

urlpatterns = [
    path('porady/', views.porady_list, name='porady_list'),
    path('porady/<int:pk>/', views.porady_detail, name='porady_detail'),
]