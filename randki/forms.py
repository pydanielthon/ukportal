from django import forms
from .models import Comment, RandkaDetail

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': 'Imię',
            'body': 'Treść'
        }
class DodajForm(forms.ModelForm):
    class Meta:
        model = RandkaDetail
        fields = ['kategoria', 'plec', 'miasto', 'tytul', 'opis', 'img']
        widgets = {
            'kategoria': forms.Select(
                 attrs={
                    'class': 'form-control'
                }
            ),
                'plec': forms.Select(
                 attrs={
                    'class': 'form-control'
                }
            ),
             'miasto': forms.TextInput(
                 attrs={
                    'class': 'form-control'
                }
            ),
            'tytul': forms.TextInput(
                 attrs={
                    'class': 'form-control'
                }
            ),
            'opis': forms.Textarea(
                 attrs={
                    'class': 'form-control'
                }
            ),
            'img': forms.FileInput(
                 attrs={
                    'class': 'form-control'
                }
            ),
         
        }