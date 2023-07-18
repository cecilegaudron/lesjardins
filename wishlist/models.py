from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    user_favourite = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='favourites'
    )
    favourite = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    slug = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.favourite.name

    class Meta:
        ordering = ('-favourite',)
