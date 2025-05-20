from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username atau Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username atau email'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )