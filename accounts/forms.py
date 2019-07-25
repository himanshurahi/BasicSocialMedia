from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

class SignUpForm(forms.Form):
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = 'Email',widget = forms.EmailInput(attrs={'class':'form-control'}),validators=[validators.EmailValidator])
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError('Please Enter Gmail Address')
    #     return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if re.match('^[a-zA-Z0-9]+$', username):
            check_username = User.objects.filter(username = username)
            if not check_username:
                return username
            else:
                raise forms.ValidationError('Username Already Taken')

        else:
            raise forms.ValidationError('Username Error')

    
    def clean_confirm_password(self):
       
        password = self.cleaned_data.get('password')
        c_password = self.cleaned_data.get('confirm_password')
        if len(password) > 20:
            raise ValidationError('Password Must less then 20')
        else:
            if password != c_password:
                raise forms.ValidationError('Password Mismatch')
            else:
                return password

        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except:
            raise forms.ValidationError('Please Enter Valid Email')
        try:
            User.objects.get(email = email)
            raise forms.ValidationError('Email Already Exist')
        except User.DoesNotExist:
            return email       


class login_form(forms.Form):
    username = forms.CharField(label = 'Username',max_length=20, widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Password',max_length=20, widget = forms.PasswordInput(attrs={'class':'form-control'})) 

        
        
        

        
        