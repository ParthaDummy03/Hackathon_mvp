from django import forms
from django.contrib.auth.forms import AuthenticationForm


class StudentLoginForm(AuthenticationForm):

    username = forms.CharField(
        label="Student ID",
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your Student ID',
            'autocomplete': 'username',
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter your Password',
            'autocomplete': 'current-password',
        })
    )
