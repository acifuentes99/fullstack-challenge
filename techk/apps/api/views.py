# -*- coding: utf-8 -*-
from django.http import JsonResponse
from apps.scraper.models import Books, Categories
from rest_framework import serializers, viewsets, generics
import json
import os


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de Libros para API
    """
    class Meta:
        model = Books
        fields = ['id', 'category_id', 'title', 'thumbnail_url', 'price',
                  'stock', 'product_description', 'upc']


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador de Categorias para API
    """
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'books']


class BooksViewSet(viewsets.ModelViewSet):
    """
    Punto de API, que permite el acceso y edición de Libros
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksByCategory(generics.ListAPIView):
    """
    Retrona la cantidad de libros totales respecto a la categoria
    seleccionada por el usuario
    """
    serializer_class = BooksSerializer

    def get_queryset(self):
        category_id = self.kwargs['category']
        return Books.objects.filter(category_id=category_id)


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    Punto de API, que permite el acceso y edición de Categorias
    """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


def fallbackJson(request):
    """
    En caso de no haber realizado el Scrapping, se retorna un JSON
    temporal, con información sobre libros y categorias
    """
    app_dir = os.path.dirname(os.path.realpath(__file__))
    book_data = json.load(open(app_dir+'/books.json'))
    return JsonResponse(book_data[0])
