# from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> None:
    """ função sobre """
    return HttpResponse("ola vc esta no home")


def sobre(request) -> None:
    """ função sobre """
    return HttpResponse("ola vc esta no sobre")

# criamos essa aplicação(app) chamada recipes para config as views dessa pagina
