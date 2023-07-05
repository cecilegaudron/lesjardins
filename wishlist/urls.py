from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourite_list, name='wishlist'),
    path('like/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
