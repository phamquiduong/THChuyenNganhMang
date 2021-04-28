from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('status/',  views.listStatus, name='adminStatus'),
    path('status/add-status',  views.addStatus, name='addStatus'),
    path('status/list-status/<int:pk>/',  views.listStatus, name='listStatus'),
    path('status/detail-status/<int:pk>/',  views.detailStatus, name='detailStatus'),
    path('status/update-status/<int:pk>/',  views.updateStatus, name='updateStatus'),
    path('status/delete-status/<int:pk>/',  views.deleteStatus, name='deleteStatus'),

    path('account/',  views.listAccount, name='account'),
    path('account/add-account',  views.addAccount, name='addAccount'),
    path('account/list-account',  views.listAccount, name='listAccount'),
    path('account/delete-account/<int:pk>/',  views.deleteAccount, name='deleteAccount'),
    path('account/detail-account/<int:pk>/',  views.detailAccount, name='detailAccount'),
    path('account/update-account/<int:pk>/',  views.updateAccount, name='updateAccount'),

    path('contest/',  views.listContest, name='listContest'),
    path('contest/list-contest',  views.listContest, name='listContest'),
    path('contest/delete-contest/<int:pk>/',  views.deleteContest, name='deleteContest'),
    path('contest/detail-contest/<int:pk>/',  views.detailContest, name='detailContest'),
    path('contest/join-contest/<int:pk>/',  views.joinContest, name='joinContest'),
    path('contest/delete-join-contest/<int:pk>/',  views.deletejoinContest, name='deletejoinContest'),

    path('language/add-language',  views.addLanguage, name='addLanguage'),
    path('language/list-language',  views.listLanguage, name='listLanguage'),
    path('language/',  views.listLanguage, name='listLanguage'),
     path('language/delete-language/<int:pk>/',  views.deleteLanguage, name='deleteLanguage'),
]
