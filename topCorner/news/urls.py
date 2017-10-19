from django.conf.urls import url
from .views import IndexView,NewsDetail

app_name = 'news'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^item/(?P<pk>\d+)$', NewsDetail.as_view(), name='detail'),

  
]