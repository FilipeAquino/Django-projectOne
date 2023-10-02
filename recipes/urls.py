# vamos deixar as coisas mais organizadas:
from django.urls import path
from recipes import views

# da nomes as urls
urlpatterns = [
    path('', views.home, name='recipes-home'),  # pagina raiz(home)
    # dessa forma essa pag vai ter uma id que a função tem acess
    path("recipes/<int:id>/", views.recipe, name='recipes-recipe')
]

# outra forma de fazer é criando a constante app_name = 'recipes' e no name=
# 'apenas o nome do link'
