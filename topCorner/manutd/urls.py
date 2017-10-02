from django.conf.urls import url

# from forms.views import IndexView
# from forms.views import MoviesView, IndexView, Movie_detail
from . import views
from django.shortcuts import render
from manutd.views import ManuView,ManuReview

app_name = 'manutd'

urlpatterns = [
    url(r'^$', ManuView.as_view(), name='home'),
    url(r'^review/(?P<pk>\d+)$', ManuReview.as_view(), name= 'review')

]
