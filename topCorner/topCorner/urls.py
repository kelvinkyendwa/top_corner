from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import login
from accounts import views
urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^home/', include('stadia.urls')),
    url(r'^arsenal/', include('arsenal.urls')),
    url(r'^manutd/', include('manutd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^news/',include('news.urls')),
    url(r'^account/', include('accounts.urls'))
  
]
