"""Collection app related urls."""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ad/$', views.movies_view, name='movies'),
    url(r'^manage_movie/$', views.manage_movie_view, name='add_movie'),
    url(r'^manage_movie/(?P<pk>[0-9]+)/$',
        views.manage_movie_view, name='manage_movie'),
    url(r'^delete_movie/(?P<pk>[0-9]+)/$',
        views.delete_movie_view, name='delete_movie'),
]
