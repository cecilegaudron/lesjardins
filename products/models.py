from django.db import models


class Category(models.Model):
    """
    Database model for categories
    """
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
    name = models.CharField(
        max_length=254,
    )
    description = models.TextField(
        max_length=800,
    )
    price_kilo = models.DecimalField(
        max_digits=3, 
        decimal_places=2,
    )
    weight = models.IntegerField(
        help_text = "Weight in grams"
    )
    price = models.DecimalField(
        max_digits=3,
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
    
    """
    For ratings
    https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
    """
    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.name}: {self.average_rating()}"


class Rating(models.Model):
    """
    Database for Ratings
    https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
    """
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.header}: {self.rating}"