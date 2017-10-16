from django.conf.urls import url
from arsenal.views import ArsenalView, ArsenalReview

app_name = 'arsenal'

urlpatterns = [
    url(r'^$', ArsenalView.as_view(), name='home'),
    url(r'^review/(?P<pk>\d+)$', ArsenalReview.as_view(), name= 'review'),
]