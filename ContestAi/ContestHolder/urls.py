from django.urls import path
from . import views

urlpatterns = [
    path('holder/',  views.HolderView.as_view(), name='holder'),
    path('holder/contest/<str:id>',  views.ContestDetail.as_view(), name='detail'),
    path('holder/contestDelete/<str:id>',  views.ContestDelete.as_view(), name='delete'),
    path('holder/create',  views.CreateContest.as_view(), name='create'),
    path('contest/status/<str:id>',  views.ContestStatus.as_view(), name='status'),

]