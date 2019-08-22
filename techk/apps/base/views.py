# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings


def index(request):
    """
    Muestra la página principal de la aplicación, dependiendo del valor de la variable
    "PROUDCTION" en config/settings.py. 
    """
    if settings.PRODUCTION:
        return render(request, 'index.html')
    else:
        return render(request, 'base/index_dev.html')
