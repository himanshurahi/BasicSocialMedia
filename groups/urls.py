"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='groups'),
    path('add/', views.add_group, name='add_group'),
    path('join/', views.join_group, name= 'join_group'),
    path('leave/', views.leave_group, name = 'leave_group'),
    path('delete/', views.delete_group, name = 'delete_group'),
    path('logout/', views.logout, name = 'logout'),
    path('<str:slug>', views.group_details, name = 'group_details'),
    path('post/', include('post.urls'))
    
]
