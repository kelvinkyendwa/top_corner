from django.conf.urls import url
from .views import IndexView

app_name = 'news'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
  
]