from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm

class SimpleLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(SimpleLoginForm, self).__init__(*args, **kwargs)
        # change fields
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email',
                                                            'class': 'form-control',
                                                             'placeholder': 'nazwa@przyklad.pl'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password',
                                                                    'class': 'form-control',

                                                                    'placeholder': '*************'})
        # change label
        self.fields['login'].label = ''
        self.fields['password'].label = ''

class SimpleSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(SimpleSignupForm, self).__init__(*args, **kwargs)
        #change fields
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email',
                                                                    'class': 'form-control',

                                                             'placeholder': 'nazwa@przyklad.pl'})
        # self.fields['email2'].widget = forms.TextInput(attrs={'type': 'email',
        #                                                       'placeholder': 'nazwa@przyklad.pl'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password',
                                                                    'class': 'form-control',

                                                                     'placeholder': '*************'})
        #change labels
        self.fields['password2'].widget = forms.PasswordInput(attrs={'type': 'password',
                                                                    'class': 'form-control',

                                                                     'placeholder': '*************'})
        # self.fields['email2'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

class SimpleResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SimpleResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email',
                                                                    'class': 'form-control',

                                                                    'placeholder': '*************'})
        self.fields['email'].label = ''
