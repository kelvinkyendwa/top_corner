from django.conf.urls import url

# from forms.views import IndexView
# from forms.views import MoviesView, IndexView, Movie_detail
from . import views
from django.shortcuts import render

app_name = 'manutd'

urlpatterns = [
    url(r'^$', views.index, name='index'),



]
