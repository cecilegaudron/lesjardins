from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('email_sent/', views.email_sent, name='email_sent'),
]
