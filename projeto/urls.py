"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# exemplo de view:


def myview(request) -> None:
    """ função exemplo """
    return HttpResponse("A resposta viria com essa função")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myview), # pagina raiz
    path('sobre/', myview)  # 1.
]


# Porta de entrada da aplicação. Vamos conseguir indicar os caminhos
# que cada url vai tomar usando apps
# 1. eu quero um caminho que aponte para algun lugar usando o path('algo/'),
# por enquanto n vai ver nada e precisa dos outros parametros.
# o view tem que receber como argumento o request e retornar um reponse
