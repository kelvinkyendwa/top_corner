from django.contrib import admin
from .models import Opinion,Pundit,Team
# Register your models here.

admin.site.register(Opinion)
admin.site.register(Pundit)
admin.site.register(Team)