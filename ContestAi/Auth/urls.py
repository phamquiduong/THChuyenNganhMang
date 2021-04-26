from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('login/',  views.Login.as_view(), name='login'),
    path('signUp/',  views.SignUp.as_view(), name='signUp'),
    path('logOut/',  views.LogOut.as_view(), name='logOut'),

]
