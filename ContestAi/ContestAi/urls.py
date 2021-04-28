from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls, name='adminSite'),
    # path('', include('devs.urls')),
    path('', include('Auth.urls')),
    path('', include('ContestHolder.urls')),
    path('', include('ContestAdmin.urls')),
    path('', include('ContestParticipant.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('django-rq/', include('django_rq.urls'))
]


