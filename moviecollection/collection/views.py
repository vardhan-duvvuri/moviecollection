"""Views.py."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Movie
from .forms.admin_form import MovieForm

# Create your views here.


def index(request):
    """Render index page."""
    movies = Movie.objects.all()
    p = Paginator(movies, 8)

    page = request.GET.get('page')
    try:
        movies_list = p.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies_list = p.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies_list = p.page(p.num_pages)

    return render(request, 'index.html', {'movies': movies_list})


def movies_view(request):
    """View all movies in table."""
    movies = Movie.objects.all()
    p = Paginator(movies, 8)

    page = request.GET.get('page')
    try:
        movies_list = p.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies_list = p.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies_list = p.page(p.num_pages)

    return render(request, 'movies.html', {'movies': movies_list})


def get_or_none(model, *args, **kwargs):
    """Function to get the object or none."""
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def manage_movie_view(request, pk=False):
    """
    Show the details for a specified movie record.

    :param pk:      The movie id
    """
    movie_data = get_or_none(Movie, id=pk)
    movie_form = MovieForm()

    if not movie_data:
        movie_form = MovieForm()
        if request.method == "POST":
            movie_form = MovieForm(request.POST)
            if movie_form.is_valid():
                new_movie = movie_form.save(commit=False)
                new_movie.save()
                return HttpResponseRedirect("/ad/")
    else:
        movie_data = Movie.objects.get(id=movie_data.id)
        movie_form = MovieForm(instance=movie_data)
        if request.method == "POST":
            movie_form = MovieForm(request.POST, instance=movie_data)
            if movie_form.is_valid():
                movie_form.save()
                return HttpResponseRedirect("/ad/")

    req_context = {}
    req_context["movie_data"] = movie_data
    req_context["movie_form"] = movie_form

    return render(request, 'manage_movie.html', req_context)


def delete_movie_view(request, pk=False):
    """
    Delete the details for a specified movie record.

    :param pk:      The movie id
    """
    movie_data = get_or_none(Movie, id=pk)

    if movie_data:
        movie_data.delete()

    return HttpResponseRedirect("/ad/")
