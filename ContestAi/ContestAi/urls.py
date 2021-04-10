from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('devs.urls')),
    path('', include('Auth.urls')),
]

urlpatterns += [
    path('django-rq/', include('django_rq.urls'))
]
