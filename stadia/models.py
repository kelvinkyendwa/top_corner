from django.db import models

# Create your models here.

class Team(models.Model):
    name = model.CharField(max_length=200)
    team_logo_url = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Pundit(models.Model):
    pundit_name = model.CharField(max_length=200)
    favorite_club =  models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.pundit_name

class Opinion(models.Model):
    reviewer = models.ForeignKey(Pundit, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = model.CharField(max_length=200)
    game_date = models.DateField(max_length=8, null=True )
    game_review = models.TextField(max_length=1000, null=True)
    logo_url = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title
