from django.conf.urls import url

# from forms.views import IndexView
# from forms.views import MoviesView, IndexView, Movie_detail
from . import views
from django.shortcuts import render
from arsenal.views import ArsenalView

app_name = 'arsenal'

urlpatterns = [
    url(r'^$', ArsenalView.as_view(), name='home'),

]
