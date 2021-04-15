from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('/detail/<int:mod>/',views.detail,name='detail')
]
