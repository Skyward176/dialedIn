from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coffeeForm', views.coffeeForm, name='coffeeForm'),
    path('extractionForm', views.extractionForm, name='extractionForm'),
    path('send_mail', views.sendMail, name='email_sender'),
]
