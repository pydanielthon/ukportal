from .models import darmowy
from django import forms


class DodajFirme(forms.ModelForm):
    class Meta:
        model = darmowy
        fields = ['kategoria', 'nazwa', 'email', 'miasto', 'numer', 'logo']
        widgets = {
            'nazwa': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'miasto': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
             'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
              'kategoria': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
          'numer': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
              'logo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        
