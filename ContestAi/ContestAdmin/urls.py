from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('status/',  views.listStatus, name='listStatus'),
    path('status/add-status',  views.addStatus, name='addStatus'),
    path('status/list-status',  views.listStatus, name='listStatus'),
    path('status/detail-status/<int:pk>/',  views.detailStatus, name='detailStatus'),
    path('status/update-status/<int:pk>/',  views.updateStatus, name='updateStatus'),
    path('status/delete-status/<int:pk>/',  views.deleteStatus, name='deleteStatus'),
]
