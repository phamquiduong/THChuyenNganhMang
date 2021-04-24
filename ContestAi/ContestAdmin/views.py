from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def addStatus(request):
    if request.POST:
        staticF = StaticForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:
        staticF = StaticForm()
        context = {
            'formStatus': staticF
        }
        return render(request, 'Status/add.html', context=context)
    else:
        return redirect('login')

def updateStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    if request.POST:
        staticF = StaticForm(request.POST, request.FILES,instance=istatus)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:      
        staticF = StaticForm(instance=istatus)
        context = {
            'formStatus': staticF
        }
        print(context)
        return render(request, 'Status/add.html', context=context)
    else:
        return redirect('login')

def listStatus(request):
    if request.user.is_superuser:
        lstatus = Status.objects.all()
        context = {
            'lstatus': lstatus
        }
        return render(request, 'Status/list.html', context=context)
    else:
        return redirect('login')

def detailStatus(request, pk):
    if request.user.is_superuser:
        istatus = Status.objects.get(pk=pk)
        context = {
            'istatus':istatus
        }
        return render(request, 'Status/detail.html', context=context)
    else:
        return redirect('login')

def deleteStatus(request, pk):
    if request.user.is_superuser:
        dstatus = Status.objects.get(pk=pk)
        dstatus.delete()
        return listStatus(request)
    else:
        return redirect('login')