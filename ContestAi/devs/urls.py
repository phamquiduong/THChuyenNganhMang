from django.urls import path
from . import views

urlpatterns = [
    path('dev/',  views.Index.as_view(), name='index'),
    path('login/',  views.Login.as_view(), name='login'),

]
