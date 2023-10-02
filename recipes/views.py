from django.shortcuts import render
from utils.recipes.factory import make_recipe
# from django.http import HttpResponse


def home(request) -> None:
    """ função sobre """
    #            request, arquivo
    return render(request, 'recipes/pages/home.html', status=200, context={
        'recipes': [make_recipe() for _ in range(10)]
        })

# recebendo o id


def recipe(request, id) -> None:
    """ função que vai retorna a pag do recipe """
    #            request, arquivo
    return render(request, 'recipes/pages/recipe-view.html',
                    status=200, context={
                    'recipe': make_recipe(),
                    'is_detail_page': True,
                })
