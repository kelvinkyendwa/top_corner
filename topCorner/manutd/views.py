from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView, DetailView
from django.views.generic.list import ListView

from stadia.models import Team,Pundit,Opinion


class ManuView(ListView):

    template_name = "manutd/index.html"
    model = Opinion

    def get_queryset(self):
        return Opinion.objects.filter(team__name__icontains='manutd')

class ManuReview(DetailView):
    template_name = "manutd/reviews.html"
    model = Opinion
