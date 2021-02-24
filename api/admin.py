from django.contrib import admin
from .models import Customers ,Recipes,Ingredients,List
# Register your models here.

Models = [Customers, Recipes, Ingredients, List]

admin.site.register(Models)