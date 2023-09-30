# vamos deixar as coisas mais organizadas:
from django.contrib import admin
from django.urls import path
from recipes.views import home, sobre


urlpatterns = [
    path('', home),  # pagina raiz(home)
    path('admin/', admin.site.urls),
    path('sobre/', sobre)  # 1. (/sobre/)
]

# Porta de entrada da aplicação. Vamos conseguir indicar os caminhos
# que cada url vai tomar usando apps
# 1. eu quero um caminho que aponte para algun lugar usando o path('algo/'),
# por enquanto n vai ver nada e precisa dos outros parametros.
# o view tem que receber como argumento o request e retornar um reponse
