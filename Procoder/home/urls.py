from django.urls import path

from home import views

urlpatterns = (
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('hire', views.hire, name='hire'),
    path('project', views.project, name='project'),

)
