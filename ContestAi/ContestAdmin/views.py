from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.user.is_staff:
        return render(request, 'index.html')
    else:
        return redirect('login')

def addStatus(request):
    if request.POST:
        staticF = StaticForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()

    staticF = StaticForm()
    context = {
        'formStatus': staticF
    }
    return render(request, 'Status/add.html', context=context)

def updateStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    if request.POST:
        staticF = StaticForm(request.POST, request.FILES,instance=istatus)
        if staticF.is_valid():
            staticF.save()
            
    staticF = StaticForm(instance=istatus)
    context = {
        'formStatus': staticF
    }
    print(context)
    return render(request, 'Status/add.html', context=context)

def listStatus(request):
    lstatus = Status.objects.all()
    context = {
        'lstatus': lstatus
    }
    if request.user.is_superuser:
        return render(request, 'Status/list.html', context=context)
    else:
        return redirect('login')

def detailStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    context = {
        'istatus':istatus
    }
    return render(request, 'Status/detail.html', context=context)

def deleteStatus(request, pk):
    dstatus = Status.objects.get(pk=pk)
    dstatus.delete()
    return listStatus(request)
    