from django import forms
from django.core import validators

class CustomUserForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput)

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username != 'admin':
    #         raise forms.ValidationError("invalid username")
    #     return username
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if password != 'admin123':
    #         raise forms.ValidationError("invalid password...pls try again!!!")
    #     return password
