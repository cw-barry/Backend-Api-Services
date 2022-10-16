from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 15)
    image = models.URLField()

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE, related_name = "images")
    image = models.URLField()

    def __str__(self):
        return self.product.title
