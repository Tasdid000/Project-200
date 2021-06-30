from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = (
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('hire', views.hire, name='hire'),
    path('project', views.project, name='project'),
    path('singup', views.handlesingup, name='handlesingup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('error', views.error, name='error'),
    path('account', views.account, name='account'),

)