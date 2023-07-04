from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    favourite = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
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
