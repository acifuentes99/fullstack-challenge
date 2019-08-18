# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import re


def scrapeCategories(request):
    """
    Realiza el Scrapping de las categorias del sitio.
    Esto, buscando el id de "side_categories" dentro del sitio principal,
    y posteriormente obteniendo el Children en el cual se encuentra el
    listado de categorias.
    """
    page = requests.get("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find("div", {"class": "side_categories"}).findChild().find("ul")

    categories = content.find_all("a")
    results = list()
    for category in categories:
        results.append(category.text.strip())

    return HttpResponse(results)
