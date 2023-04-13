from django.db import models


class Category(models.Model):
    """
    Database model for categories
    """
    # Tell Django to write the correct plurial name
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Database model for product
    """
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=254,
    )
    description = models.TextField(
        max_length=800,
    )
    price_kilo = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    weight = models.IntegerField(
        help_text="Weight in grams"
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
