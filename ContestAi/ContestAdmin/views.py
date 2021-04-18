from django.shortcuts import render,redirect
from .forms import *
from django.templatetags.static import static
from datetime import datetime
import pytz
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

def listStatus(request, pk):
    lstatus = Status.objects.filter(IDcontest = pk)
    for s in lstatus:
        s.username =  User.objects.filter(id = s.IDUser)[0].username
    
    context = {
        'lstatus': lstatus,
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


def listContest(request):
    lcontest = Contest.objects.all()
    for s in lcontest:
        start = s.TimeStart
        end = s.TimeEnd
        now = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
        s.time = str(now)
        if str(now) < str(end) and str(now) > str(start):
            s.status = True
        else:
            s.status = False
        print(s.IDUser)
        try:
            name = User.objects.filter(id = s.IDUser)
            s.username = name[0].username
        except:
            print("An exception occurred")
        
    context = {
        'lcontest': lcontest
    }
    return render(request, 'Contest/list.html', context=context)

def detailContest(request, pk):
    
    icontest = Contest.objects.get(pk=pk)
    url = static('contest/a.pdf')
    icontest.url = url
    context = {
        'icontest':icontest
    }
    return render(request, 'Contest/detail.html', context=context)

def deleteContest(request, pk):
    dcontest = Contest.objects.get(pk=pk)
    dcontest.delete()
    return listContest(request)

def joinContest(request, pk):
    lstatus = RegisterContest.objects.filter(IDContest = pk)
    for s in lstatus:
        obj = Contest.objects.filter(id = s.IDContest)
        s.title = obj[0].Title

    for s in lstatus:
        obj = User.objects.filter(id = s.IDUser)
        s.username = obj[0].username

    context = {
        'lstatus': lstatus
    }
    return render(request, 'Contest/join.html', context=context)

def deletejoinContest(request, pk):
    pk_contest = RegisterContest.objects.filter(pk = pk)[0].IDContest
    duser = RegisterContest.objects.get(pk=pk)
    duser.delete()
    return joinContest(request, pk_contest)


def listLanguage(request):
    llanguage = Language.objects.all()
    context = {
        'llanguage': llanguage
    }
    return render(request, 'language/list.html', context=context)

def addLanguage(request):
    if request.POST:
        staticF = LanguageForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()

    staticF = LanguageForm()
    context = {
        'formLanguage': staticF
    }
    return render(request, 'language/add.html', context=context)
    
def deleteLanguage(request, pk):
    dlanguage = Language.objects.get(pk=pk)
    dlanguage.delete()
    return listLanguage(request)