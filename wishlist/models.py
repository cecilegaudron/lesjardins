from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(
        User,
        related_name='whishlist',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='whishlist',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name
