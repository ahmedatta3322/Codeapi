from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
class Recipes(models.Model):
    title = models.CharField(max_length=30)
    perpare = models.CharField(max_length=30)
    images = ArrayField(models.CharField(max_length=30))