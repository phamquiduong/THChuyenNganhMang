from django.shortcuts import render
from django.views import View
from django import template
from . import models


class Index(View):
    template = 'index/index.html'
    obj = models.Dev.objects.get(id=1)
    context = {
        "name": "Tue Anh Truong",
        "language": ["Python", "JS", "C#", "C++", "Java"],
        "condition": False,
        "data": obj,
    }

    def get(self, request):
        return render(request, self.template, self.context)


class Login(View):
    template = 'login/login.html'

    def get(self, request):
        return render(request, self.template)
