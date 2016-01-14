from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Chain(models.Model):
    """High-level retail chain model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slogan = models.CharField(max_length=500)
    founded_date = models.CharField(max_length=500)
    website = models.URLField(max_length=500)


class Store(models.Model):
    """Store location model. Foreign key to Chain"""
    chain = models.ForeignKey(Chain)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    opening_date = models.DateTimeField(default=timezone.now())

    # Business Hours