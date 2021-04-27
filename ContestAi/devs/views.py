from django.shortcuts import render,redirect
from django.views import View
from django import template
from . import models
import django_rq
import rq 

def run_tester(s):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location('tester', './static/contest/contest1/tester.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules['tester'] = module
    spec.loader.exec_module(module)
    obj = models.Dev.objects.get(id=3)
    try:
        obj.userDescription=module.check_python(s)
    except rq.timeouts.JobTimeoutException:
        obj.userDescription="TLE"
    except:
        obj.userDescription="Compile Error"
    obj.save()

def run_tester_cpp(s):
    import importlib
    import sys
    spec = importlib.util.spec_from_file_location('tester', './static/contest/contest1/tester.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules['tester'] = module
    spec.loader.exec_module(module)
    obj = models.Dev.objects.get(id=3)
    try:
        obj.userDescription=module.check_cpp(s)
    except rq.timeouts.JobTimeoutException:
        obj.userDescription="TLE"
    except:
        obj.userDescription="Compile Error"
    obj.save()

class Index(View):
    template = 'index/index.html'
    obj = models.Dev.objects.get(id=3)
    context = {
        "name": "Truong Quang Hung",
        "language": ["Python", "JS", "C#", "C++", "Java"],
        "condition": True,
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
        try:
            f = request.FILES["file"]
            name = str(f)
            print(name)
            if ".py" in name:
                with open('./static/contest/contest1/test.py', 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                obj = models.Dev.objects.get(id=3)
                obj.userDescription='Pending'
                obj.save()
                c=10
                queue = django_rq.get_queue('default',default_timeout=c)
                queue.enqueue(run_tester,'test',result_ttl=0)   
            if ".cpp" in name:
                with open('./static/contest/contest1/test.cpp', 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                obj = models.Dev.objects.get(id=3)
                obj.userDescription='Pending'
                obj.save()
                c=5
                queue = django_rq.get_queue('default',default_timeout=c)
                queue.enqueue(run_tester_cpp,'test',result_ttl=0) 
        except:
            print("No File select")  
        return redirect('/')

# class Login(View):
#     template = 'login/login.html'

#     def get(self, request):
#         return render(request, self.template)
