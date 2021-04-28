from django.urls import path
from . import views

urlpatterns = [
    path('participant/',  views.ParticipantView.as_view(), name='participant'),
    path('register/<str:id>',  views.Register.as_view(), name='register'),
    path('start/<str:id>',  views.Starting.as_view(), name='start'),
    path('standing/<str:id>',  views.Standing.as_view(), name='standing'),
]
