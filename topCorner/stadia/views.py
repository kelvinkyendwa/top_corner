from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView,CreateView

# Create your views here.
class IndexView(TemplateView):

    template_name = "home.html"
