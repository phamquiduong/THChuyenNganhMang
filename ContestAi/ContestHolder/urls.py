from django.urls import path
from . import views

urlpatterns = [
    path('holder/',  views.HolderView.as_view(), name='holder'),
]