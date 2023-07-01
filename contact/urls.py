from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('email-sent.html', views.email_sent, name='email-sent'),
]
