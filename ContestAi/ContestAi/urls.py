from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('devs.urls')),
    path('', include('Auth.urls')),
    path('', include('ContestHolder.urls')),
    path('', include('ContestParticipant.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
