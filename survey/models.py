from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Survey(models.Model):

    ConsumerAges = [
        ("18-25", "18-25 years"),
        ("26-35", "26-35 years"),
        ("36-45", "36-45 years"),
        ("46-59", "46-59 years"),
        ("60", "60 years and +"),
    ]
    ConsumerRatings = [
        ("extraordinary", "Extraordinary"),
        ("perfect", "Perfect"),
        ("no-complaints", "No complaints"),
        ("can-be-better", "Can be better"),
        ("not-recommended", "Not recommended"),
    ]
    ConsumerReasons = (
        ('reason_organic', 'They are organic'),
        ('reason_healthy', 'They are good for your health'),
        ('reason_fresh', 'They are fresh'),
        ('reason_taste', 'They taste good'),
        ('reason_close', 'They are close to home')
    )
    ratings = models.CharField(
        "Are you satisfied with our offer and service?",
        blank=False,
        choices=ConsumerRatings,
        max_length=54
    )
    age = models.CharField(
        "How old are you?",
        blank=True,
        choices=ConsumerAges,
        max_length=54
    )
    reason = MultiSelectField(
        "Why do you buy our products?",
        blank=False,
        max_choices=5,
        choices=ConsumerReasons
    )
    comments = models.TextField(
        "Do you have any comments?",
        max_length=254,
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Satisfaction: "{self.ratings}"'

    def get_absolute_url(self):
        return reverse('survey')
