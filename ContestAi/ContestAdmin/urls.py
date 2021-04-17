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

    path('account/',  views.listAccount, name='listAccount'),
    path('account/add-account',  views.addAccount, name='addAccount'),
    path('account/list-account',  views.listAccount, name='listAccount'),
    path('account/delete-account/<int:pk>/',  views.deleteAccount, name='deleteAccount'),
    path('account/detail-account/<int:pk>/',  views.detailAccount, name='detailAccount'),
    path('account/update-account/<int:pk>/',  views.updateAccount, name='updateAccount'),
]
