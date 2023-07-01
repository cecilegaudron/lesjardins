from django.urls import path
from . import views


urlpatterns = [
    path('', views.survey_create, name='survey'),
    path('success.html', views.success, name='success'),
]