from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('/participant/',  views.ParticipantView.as_view(), name='participant'),
    path('/register/<str:id>',  views.Register.as_view(), name='register'),
]
