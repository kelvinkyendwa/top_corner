from stadia.models import Opinion,Pundit,Team
from django import forms


class OpinionForm(forms.ModelForm):
    model = Opinion
    fields = []