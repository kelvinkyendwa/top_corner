from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from stadia.models import Team,Pundit,Opinion


def index(request):
    latest_reviews = Opinion.objects.filter(team="manutd")
    context = {'latest_reviews': latest_reviews}
    return render(request, 'manutd/index.html')
