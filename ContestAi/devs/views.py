from django.shortcuts import render
from django.views import View
from django import template
from . import models


class Index(View):
    template = 'index/index.html'
    obj = models.Dev.objects.get(id=1)
    test = {"id": 1}
    context = {
        "name": "Tue Anh Truong",
        "language": ["Python", "JS", "C#", "C++", "Java"],
        "condition": False,
        "data": obj,
    }

    def get(self, request):
        print(self.test.get("id"))
        if self.test.get("id") == 3:
            self.test.update({"id": 1})
        else:
            self.test.update({"id": 3})
        if self.context.get('data') == models.Dev.objects.get(id=1):
            obj_new = models.Dev.objects.get(id=3)
            self.context.update({"data": obj_new})
        else:
            obj_new = models.Dev.objects.get(id=1)
            self.context.update({"data": obj_new})
        return render(request, self.template, self.context)

    def post(self, request):
        f = request.FILES["file1"]
        with open('./static/demo/test1.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        f = request.FILES["file2"]
        with open('./static/demo/test2.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return Index.get(self,request)

# class Login(View):
#     template = 'login/login.html'

#     def get(self, request):
#         return render(request, self.template)
