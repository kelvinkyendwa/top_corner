from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=200)
    team_logo_url = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Pundit(models.Model):
    pundit_name = models.CharField(max_length=200)
    favorite_club =  models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.pundit_name

class Opinion(models.Model):
    reviewer = models.ForeignKey(Pundit, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    game_date = models.DateField(max_length=8, null=True )
    game_review = models.TextField(max_length=1000, null=True)
    logo_url = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title