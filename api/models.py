from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    

class Ingredients(models.Model):
    title = models.CharField(max_length=30)
    images = ArrayField(models.CharField(max_length=30))
    price = models.IntegerField()
    

class Recipes(models.Model):
    title = models.CharField(max_length=30)
    perpare = models.CharField(max_length=30)
    images = ArrayField(models.CharField(max_length=30))
    ingredients = models.ManyToManyField(Ingredients)
class List(models.Model):
    ingredients = models.ManyToManyField(Ingredients)
    recipes = models.ManyToManyField(Recipes)
    customers = models.ForeignKey(Customers,on_delete=models.CASCADE)