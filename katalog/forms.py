from .models import katalog
from django import forms


class DodajFirme(forms.ModelForm):
    class Meta:
        model = katalog
        fields = ['category', 'name', 'mail', 'adres', 'telefon', 'image']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'adres': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'mail': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
              'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
          'telefon': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
              'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        labels = {
            'name': 'Nazwa Firmy',
            'category': 'Kategoria',
            'mail': 'Email Firmowy',
            'adres': 'Adres Firmy',
            'telefon': 'Numer Telefonu',
            'image': 'Logo Firmy'
        }
