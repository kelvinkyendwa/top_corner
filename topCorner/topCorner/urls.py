from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import login

urlpatterns = [
    url(r'^$', include('stadia.urls')),
    url(r'^arsenal/', include('arsenal.urls')),
    url(r'^manutd/', include('manutd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^news/',include('news.urls')),
    url(r'^account/', include('accounts.urls'))
  
]
