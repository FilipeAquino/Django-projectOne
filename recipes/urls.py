# vamos deixar as coisas mais organizadas:
from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.home),  # pagina raiz(home)
    # dessa forma essa pag vai ter uma id que a função tem acess
    path("recipes/<int:id>/", views.recipe)
]
