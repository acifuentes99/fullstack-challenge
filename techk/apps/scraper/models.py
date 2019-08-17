# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categories(models.Model):
    """
    Modelo de Categorias
    """
    name = models.CharField(max_length=254)

class Books(models.Model):
    """
    Modelo de Libros
    """
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=2048)
    thumbail_url = models.CharField(max_length=2048)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    description = models.TextField()
    upc = models.CharField(max_length=32)
