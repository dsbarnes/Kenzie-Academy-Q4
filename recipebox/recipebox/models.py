from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=15)
    instructions = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    user = models.OneToOneField(User, models.CASCADE, null=True)
    favorites = models.ManyToManyField(Recipe, related_name='favorites')

    def __str__(self):
        return self.name