# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .models import Books, Categories
import requests


def scrapeBooks(request, pages=1):
    """
    Realiza el proceso de Scrapping de un libro.
    Esto, consultando la página de listado de libros, y posteriormente
    realizando un Scrapping de cada libro en la lista.
    """
    if not Categories.objects.all().exists():
        scrapeCategories() 
    base_url = "http://books.toscrape.com/"
    for page in range(1, pages+1):
        page = requests.get(base_url+"catalogue/page-"+str(page)+".html")
        soup_list = BeautifulSoup(page.content, 'html.parser')
        list_content = soup_list.find("ol", {"class": "row"}).find_all("article")
        for book in list_content:
            book_title = book.find_all("a")[1]['title']
            book_href = book.find("a")['href']
            book_url = base_url+"catalogue/"+book_href
            if not Books.objects.filter(title=book_title).exists() :
                book_page = requests.get(book_url)
                book_soup = BeautifulSoup(book_page.content, 'html.parser')
                book_data = getBookDict(book_soup, book_url)
                Books.objects.create(**book_data)
    return HttpResponse(status=204)


def scrapeCategories():
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
    for category in categories:
        Categories.objects.create(name=category.text.strip())
    return HttpResponse(status=204)


def getBookDict(book_soup, book_url):
    """
    Retorna diccionario, con los elementos necesarios del Scrapping para 
    poder ser almacenados en la base de datos
    NOTA: Existen descripciones nulas dentro de la página de libros,
    por lo que se revisa si existe la descripción del producto, de lo
    contrario se guarda como vacia.
    """
    description_soup = book_soup.find("div", {"id": "product_description"})
    if description_soup:
        description = description_soup.find_next("p").text.strip()
    else:
        description = None
    return {
        'category': Categories.objects.get(name=book_soup .find("ul", {"class": "breadcrumb"}) .find_all("a")[2].text.strip()),
        'title': book_soup.find("h1").text.strip(),
        'thumbnail_url': book_url+"/../"+str(book_soup.find("div", {"class": "thumbnail"}).find("img")['src']),
        'price': book_soup.find("p", {"class": "price_color"}).text.strip().replace("£", ""),
        'stock': True if book_soup.find("p", {"class": "instock"}).find("i")['class'][0] == 'icon-ok' else False,
        'product_description': description,
        'upc': book_soup.find("table").find("td").text.strip()
    }
