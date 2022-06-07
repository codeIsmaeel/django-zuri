from unicodedata import name
from django.db import models
from django.forms import modelformset_factory

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
