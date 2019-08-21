# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup
from .models import Books, Categories
import requests


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
    for category in categories:
        Categories.objects.create(name=category.text.strip())
    return HttpResponse("Categories Created")


def scrapeBooks(request):
    """
    Realiza el proceso de Scrapping de un libro.
    Esto, consultando la página de listado de libros, y posteriormente
    realizando un Scrapping de cada libro en la lista.
    """
    base_url = "http://books.toscrape.com/"
    #pages = 50
    pages = 2
    for page in range(1, pages+1):
        page = requests.get(base_url+"catalogue/page-"+str(page)+".html")
        soup_list = BeautifulSoup(page.content, 'html.parser')
        list_content = soup_list.find("ol", {"class": "row"}).find_all("article")
        books = list()
        for book in list_content:
            book_href = book.find("a")['href']
            book_url = base_url+"catalogue/"+book_href
            book_page = requests.get(book_url)
            book_soup = BeautifulSoup(book_page.content, 'html.parser')
            book_data = {
                'category': Categories.objects.get(name=book_soup .find("ul", {"class": "breadcrumb"}) .find_all("a")[2].text.strip()),
                'title': book_soup.find("h1").text.strip(),
                'thumbnail': book_url+"/../"+str(book_soup.find("div", {"class": "thumbnail"}).find("img")['src']),
                'price': book_soup.find("p", {"class": "price_color"}).text.strip().replace("£", ""),
                'stock': True if book_soup.find("p", {"class": "instock"}).find("i")['class'][0] == 'icon-ok' else False,
                'description': book_soup.find("div", {"id": "product_description"}).find_next("p").text.strip(),
                'upc': book_soup.find("table").find("td").text.strip()
            }
            books.append(book_soup.prettify())
            Books.objects.create(**book_data)
    return JsonResponse("Books scraped!")


"""
for book in list_content:
    book_href = book.find("a")['href']
    book_page = requests.get(base_url+book_href)
    book_soup = BeautifulSoup(page.content, 'html.parser')
    books.append(book_soup.prettify())



                    'has_stock': True if book_soup.find("p", {"class": "instock"}).find("i")['class'][0] == 'icon-ok' else False,
                    'stock': book_soup.find("p", {"class": "instock"}).text.strip(),
"""
