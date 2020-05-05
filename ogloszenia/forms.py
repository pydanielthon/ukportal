from .models import Comment, Dodaj
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

class DodajForm(forms.ModelForm):
    class Meta:
        model = Dodaj
        fields = ['kategoria', 'tytul', 'tresc']
        widgets = {
            'kategoria': forms.Select(
                 attrs={
                    'class': 'form-control'
                }
            ),
            'tytul': forms.TextInput(
                 attrs={
                    'class': 'form-control'
                }
            ),
            'tresc': forms.Textarea(
                 attrs={
                    'class': 'form-control'
                }
            ),
        }