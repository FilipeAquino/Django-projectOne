from django.shortcuts import render
# from django.http import HttpResponse


def home(request) -> None:
    """ função sobre """
    #            request, arquivo
    return render(request, 'recipes/home.html')


def sobre(request) -> None:
    """ função sobre """
    return render(request, 'recipes/sobre.html')

# criamos essa aplicação(app) chamada recipes para config as views dessa pagina
# quando um cliente faz um get ele quer receber uma pagina e é mto
# desnecessario escrever tudo na mão, por isso vamos usar o render para
# rederizar um arquivo html
