from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from .models import  Groups
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import forms
from post.models import Post
# Create your views here.
@login_required
def home(request):
    groups = Groups.objects.all()
    return render(request, 'all_groups.html',{'groups':groups})

@login_required
def add_group(request):
    groups = User.objects.get(id = request.user.id).members.all()
    
    
    
    form = forms.add_group()
    if request.method == 'POST':
        form = forms.add_group(request.POST)
        if form.is_valid():
            
            group = Groups()
            group.name = form.cleaned_data.get('name')
            group.description = form.cleaned_data.get('desc')
            groups.user = request.user.id
            group.slug = group.unique_slug()
            group.group_admin = request.user
            group.save()
            Groups.objects.get(id = group.id).members.add(request.user.id)
            

            
            return redirect('add_group')




    return render(request,'add_group.html',{'form':form,'groups':groups})

@login_required
def join_group(request):
    if request.method == 'POST':
        if request.POST['group_id']:
            Groups.objects.get(id = request.POST['group_id']).members.add(request.user.id)
            # return redirect('add_group')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def leave_group(request):
    if request.method == 'POST':
        if request.POST['group_id']:
            Groups.objects.get(id = request.POST['group_id']).members.remove(request.user.id)
            # return redirect('add_group')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_group(request):
    if request.method == 'POST':
        Groups.objects.filter(id = request.POST['group_id']).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return redirect('groups')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required
def group_details(request, slug):
    group = Groups.objects.filter(slug = slug).first()
    request.session['group_id'] = group.id
    posts = Post.objects.filter(group_id = group.id)
    
    return render(request, 'group_posts.html',{'posts':posts})
