from django.shortcuts import render
from django.views import View
from django import template
from . import models
from django_rq import job

@job
def run_tester(s):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location('tester', './static/contest/contest1/tester.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules['tester'] = module
    spec.loader.exec_module(module)
    #contest = importlib.import_module('./static/contest/contest1/tester', package=None)
    obj = models.Dev.objects.get(id=3)
    obj.userDescription=module.check(s)
    obj.save()

class Index(View):
    template = 'index/index.html'
    obj = models.Dev.objects.get(id=3)
    context = {
        "name": "Tue Anh Truong",
        "language": ["Python", "JS", "C#", "C++", "Java"],
        "condition": False,
        "data": obj,
    }

    def get(self, request):
        # print(self.test.get("id"))
        # if self.test.get("id") == 3:
        #     self.test.update({"id": 1})
        # else:
        #     self.test.update({"id": 3})
        # if self.context.get('data') == models.Dev.objects.get(id=1):
        #     obj_new = models.Dev.objects.get(id=3)
        #     self.context.update({"data": obj_new})
        # else:
        #     obj_new = models.Dev.objects.get(id=1)
        #     self.context.update({"data": obj_new})
        # new=models.Dev.objects.create(userName="testDB", userDescription="Test DB", userAge="hello")
        # new.save()
        obj_new = models.Dev.objects.get(id=3)
        self.context.update({"data": obj_new})
        return render(request, self.template, self.context)

    def post(self, request):
        # temp=models.Dev.objects.last()
        # print(temp.id)
        f = request.FILES["file"]
        with open('./static/contest/contest1/test.pkl', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        obj = models.Dev.objects.get(id=3)
        obj.userDescription='Pending'
        obj.save()
        run_tester.delay('tester')
        return Index.get(self,request)

# class Login(View):
#     template = 'login/login.html'

#     def get(self, request):
#         return render(request, self.template)
