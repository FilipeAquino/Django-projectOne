# vamos deixar as coisas mais organizadas:
from django.urls import path
from recipes.views import home


urlpatterns = [
    path('', home),  # pagina raiz(home)
]
