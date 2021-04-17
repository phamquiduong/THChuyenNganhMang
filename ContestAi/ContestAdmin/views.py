from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def addStatus(request):
    if request.POST:
        staticF = StatusForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()

    staticF = StatusForm()
    context = {
        'formStatus': staticF
    }
    return render(request, 'Status/add.html', context=context)

def updateStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    if request.POST:
        staticF = StatusForm(request.POST, request.FILES,instance=istatus)
        if staticF.is_valid():
            staticF.save()
            
    staticF = StatusForm(instance=istatus)
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
    return render(request, 'Status/list.html', context=context)

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
    
def addAccount(request):
    if request.POST:
        staticF = UserForm(request.POST, request.FILES)

        if staticF.is_valid():
            user = staticF.save()
            user.set_password(user.password)
            user.save()
            print("User:",user.password)

    staticF = UserForm()
    context = {
        'formUser': staticF
    }
    return render(request, 'User/add.html', context=context)

def updateAccount(request,pk):
    isuser = User.objects.get(pk=pk)
    if request.POST:
        staticF = UserForm(request.POST, request.FILES,instance=isuser)
        if staticF.is_valid():
            staticF.save()
            
    staticF = UserForm(instance=isuser)
    context = {
        'formUser': staticF
    }
    print(context)
    return render(request, 'User/add.html', context=context)

def listAccount(request):
    luser = User.objects.all()
    context = {
        'luser': luser
    }
    return render(request, 'User/list.html', context=context)

def detailAccount(request,pk):
    isuser = User.objects.get(pk=pk)
    context = {
        'isuser':isuser
    }
    return render(request, 'User/detail.html', context=context)

def deleteAccount(request, pk):
    duser = User.objects.get(pk=pk)
    duser.delete()
    return listAccount(request)
