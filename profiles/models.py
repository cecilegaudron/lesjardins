from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """User profile model to save delivery information and order history"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_country = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    # Existing user: just save the profile
    instance.userprofile.save()
