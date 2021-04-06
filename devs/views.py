from django.shortcuts import render
from django.views import View
from django import template


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
