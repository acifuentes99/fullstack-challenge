# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Categories(models.Model):
    """
    Modelo de Categorias
    """
    name = models.CharField(max_length=254)


class Books(models.Model):
    """
    Modelo de Libros
    """
    category = models.ForeignKey(Categories, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=2048)
    thumbnail_url = models.CharField(max_length=2048)
    price = models.FloatField()
    stock = models.BooleanField(default=False)
    product_description = models.TextField(default=None, blank=True, null=True)
    upc = models.CharField(max_length=32)
