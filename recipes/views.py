from django.shortcuts import render
# from django.http import HttpResponse


def home(request) -> None:
    """ função sobre """
    #            request, arquivo
    return render(request, 'recipes/pages/home.html', status=200, context={
        "name": "Luiz filipe"
        })
