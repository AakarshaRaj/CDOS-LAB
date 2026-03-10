from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Movie
# from django.http import Http404
# Create your views here.
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("You are at the movies index page.")


def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movies/index.html', context)
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/show.html', {'movie': movie})

    
