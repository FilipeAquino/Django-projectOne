from django.shortcuts import render
# from django.http import HttpResponse


def home(request) -> None:
    """ função sobre """
    #            request, arquivo
    return render(request, 'recipes/pages/home.html', status=200, context={
        "name": "Luiz filipe"
        })

# recebendo o id


def recipe(request, id) -> None:
    """ função que vai retorna a pag do recipe """
    #            request, arquivo
    return render(request, 'recipes/pages/recipe-view.html',
                    status=200, context={
                    "name": "Luiz filipe"
                })
