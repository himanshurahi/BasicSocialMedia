from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from . import forms
from .models import Post
from groups.models import Groups
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    group = Groups.objects.filter(id = request.session['group_id']).first()
    if group is None:
        return redirect('groups')
    if request.user not in group.members.all():
        messages.error(request, 'Please Join Group First.')
        return redirect('groups')
    
    form = forms.add_post()
    if request.method == 'POST':
        
        group_slug = group.slug
        form = forms.add_post(request.POST)
        if form.is_valid():
            posts = Post()
            posts.title = form.cleaned_data.get('title')
            posts.body = form.cleaned_data.get('body')
            posts.user_id = request.user.id
            posts.group_id = request.session['group_id']
            posts.slug = posts.unique_slug()
            
            posts.save()
            
            return redirect('group_details',slug = group_slug)
    return render(request,'add_post.html',{'forms':form})
@login_required
def delete_post(request):
    p = Post.objects.filter(id = request.POST['post_id']).first()
    if p is not None:
        if request.method == 'POST':
            if p.user.id == request.user.id:
                p.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('groups')

@login_required
def post_details(request, post_slug):
    post = Post.objects.filter(slug = post_slug).first()
    return render(request, 'post_details.html',{'posts':post}) 
       