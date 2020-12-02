from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path('addBlogPost', views.addBlogPost, name='addBlogPost'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
    
    
