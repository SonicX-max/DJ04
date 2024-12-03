from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Представление для списка фильмов
def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/list_films.html', {'films': films})

# Представление для добавления нового фильма
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')  # Перенаправление на список фильмов
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})