"""All models related to collections app."""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
    """To store all the movie info."""

    title = models.CharField(max_length=200)
    release_date = models.DateField()
    description = models.CharField(max_length=200)
    gross = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    imdb_url = models.CharField(max_length=2000)
    trailer_url = models.CharField(max_length=2000)
    length = models.IntegerField()
    imdb_rating = models.FloatField()
    poster = models.CharField(max_length=300)
