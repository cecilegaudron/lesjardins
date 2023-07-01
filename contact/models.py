from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    message_name = models.CharField(
        "Your name*",
        max_length=254,
        null=False,
        blank=False
    )
    message_email = models.EmailField(
        "Your email address",
        null=False,
        blank=False
    )
    message_mobile = models.CharField(
        "Your phone number",
        max_length=14,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
    )
    message = models.TextField(
        "Your message*",
        max_length=254,
    )
    created_on = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Message from "{self.message_name}" on {self.created_on}'
