from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from . import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def login(request):
    form = forms.login_form()
    if request.method == 'POST':
        form = forms.login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            f = auth.authenticate(username = username, password = password)
            if f is not None:
                auth.login(request,f)
                return redirect('dashboard')
            else:
                return render(request,'login.html',{'error':'Username OR Password Invalid','forms':form})

            
            
            
    return render(request, 'login.html',{'forms':form})


def signup(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username = username, email=email, password=password)
            messages.success(request,'You Can Login Now')
            return redirect('login')
        else:
            print('Error in Froms')

    
    
    # if request.method == 'POST':
    #     if re.match('^[a-zA-z0-9]+$', request.POST['username']):
    #         try:
    #             validate_email(request.POST['email'])
    #             if request.POST['password'] == request.POST['c_password']:
    #                 return HttpResponse('Store the daata')
    #             else:
    #                 return render(request,'signup.html',{'password_confirm_error':'Password Mismatch'})
    #         except ValidationError:
    #             return render(request,'signup.html',{'email_errors':'Email error'})
            

            
    #     else:
    #         return render(request,'signup.html',{'username_error':'Username error'})

   
    return render(request, 'signup.html',{'forms':form})