from django.conf.urls import url

# from forms.views import IndexView
from stadia.views import  IndexView


app_name = 'stadia'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

]
