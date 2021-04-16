from django.urls import path
from . import views

urlpatterns = [
    path('participant/',  views.ParticipantView.as_view(), name='participant'),
]
