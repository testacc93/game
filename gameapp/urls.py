from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('invest', views.invest, name='invest'),
    path('contact', views.contact, name='contact'),


]