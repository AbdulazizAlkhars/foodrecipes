from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Catagory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipesapp/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('catagories-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


# Ingredients Model


class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ingredients-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

# Recipes Model


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipesapp/images/', null=True)
    ingredients = models.ManyToManyField(Ingredient)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
