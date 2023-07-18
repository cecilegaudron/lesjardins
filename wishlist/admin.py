from django.contrib import admin
from django.db.models import Count
from .models import Wishlist


# https://realpython.com/customize-django-admin-python/
#https://stackoverflow.com/questions/32443471/django-show-the-count-of-related-objects-in-admin-list-display
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    View to display wishlist in Admin Panel
    """
    list_display = ("favourite", "user_favourite", "view_wishproduct")
    
    def view_wishproduct(self, obj):
        return obj.view_wishproduct

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(view_wishproduct=Count("user_favourite"))
        return queryset
