from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView, DetailView,View
from django.views.generic.list import ListView
from arsenal.forms import OpinionForm

from stadia.models import Team,Pundit,Opinion


class ArsenalView(ListView):

    template_name = "arsenal/index.html"
    model = Opinion

    def get_queryset(self):
        return Opinion.objects.filter(team__name__icontains='arsenal')

class ArsenalReview(DetailView):
    template_name = "arsenal/reviews.html"
    model = Opinion

