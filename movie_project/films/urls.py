from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),  # Главная страница со списком фильмов
    path('add/', views.add_film, name='add_film'),  # Страница для добавления фильма
]