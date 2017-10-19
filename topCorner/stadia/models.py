from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone= models.IntegerField(default=0)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Team(models.Model):
    name = models.CharField(max_length=200)
    team_logo_url = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Pundit(models.Model):
    pundit_name = models.CharField(max_length=200)
    favorite_club = models.ForeignKey(Team, on_delete=models.CASCADE) 
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