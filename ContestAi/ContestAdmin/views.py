from django.shortcuts import render,redirect
from .forms import *
from django.templatetags.static import static
from datetime import datetime
import pytz
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def addStatus(request):
    if request.POST:
        staticF = StatusForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:
        staticF = StatusForm()
        context = {
            'formStatus': staticF
        }
        return render(request, 'Status/add.html', context=context)
    else:
        return redirect('login')

def updateStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    if request.POST:
        staticF = StatusForm(request.POST, request.FILES,instance=istatus)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:
        staticF = StatusForm(instance=istatus)
        context = {
            'formStatus': staticF
        }
        print(context)
        return render(request, 'Status/add.html', context=context)
    else:
        return redirect('login')

def listStatus(request, pk):
    lstatus = Status.objects.filter(IDcontest = pk)
    for s in lstatus:
        s.username =  User.objects.filter(id = s.IDUser)[0].username
    if request.user.is_superuser:
        context = {
            'lstatus': lstatus,
        }
        return render(request, 'Status/list.html', context=context)
    else:
        return redirect('login')

def detailStatus(request, pk):
    istatus = Status.objects.get(pk=pk)
    if request.user.is_superuser:
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
    
def addAccount(request):
    if request.POST:
        staticF = UserForm(request.POST, request.FILES)

        if staticF.is_valid():
            user = staticF.save()
            user.set_password(user.password)
            user.save()
            print("User:",user.password)
    if request.user.is_superuser:
        staticF = UserForm()
        context = {
            'formUser': staticF
        }
        return render(request, 'User/add.html', context=context)
    else:
        return redirect('login')

def updateAccount(request,pk):
    isuser = User.objects.get(pk=pk)
    if request.POST:
        staticF = UserForm(request.POST, request.FILES,instance=isuser)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:        
        staticF = UserForm(instance=isuser)
        context = {
            'formUser': staticF
        }
        print(context)
        return render(request, 'User/add.html', context=context)
    else:
        return redirect('login')

def listAccount(request):
    luser = User.objects.all()
    if request.user.is_superuser:
        context = {
            'luser': luser
        }
        return render(request, 'User/list.html', context=context)
    else:
        return redirect('login')

def detailAccount(request,pk):
    isuser = User.objects.get(pk=pk)
    if request.user.is_superuser:
        context = {
            'isuser':isuser
        }
        return render(request, 'User/detail.html', context=context)
    else:
        return redirect('login')

def deleteAccount(request, pk):
    duser = User.objects.get(pk=pk)
    if request.user.is_superuser:
        duser.delete()
        return listAccount(request)
    else:
        return redirect('login')


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
    if request.user.is_superuser:    
        context = {
            'lcontest': lcontest
        }
        return render(request, 'Contest/list.html', context=context)
    else:
        return redirect('login')

def detailContest(request, pk):
    
    icontest = Contest.objects.get(pk=pk)
    url = static('contest/a.pdf')
    icontest.url = url
    if request.user.is_superuser:
        context = {
            'icontest':icontest
        }
        return render(request, 'Contest/detail.html', context=context)
    else:
        return redirect('login')

def deleteContest(request, pk):
    dcontest = Contest.objects.get(pk=pk)
    if request.user.is_superuser:
        dcontest.delete()
        return listContest(request)
    else:
        return redirect('login')

def joinContest(request, pk):
    lstatus = RegisterContest.objects.filter(IDContest = pk)
    for s in lstatus:
        obj = Contest.objects.filter(id = s.IDContest)
        s.title = obj[0].Title

    for s in lstatus:
        obj = User.objects.filter(id = s.IDUser)
        s.username = obj[0].username
    if request.user.is_superuser:
        context = {
            'lstatus': lstatus
        }
        return render(request, 'Contest/join.html', context=context)
    else:
        return redirect('login')

def deletejoinContest(request, pk):
    pk_contest = RegisterContest.objects.filter(pk = pk)[0].IDContest
    duser = RegisterContest.objects.get(pk=pk)
    if request.user.is_superuser:
        duser.delete()
        return joinContest(request, pk_contest)
    else:
        return redirect('login')


def listLanguage(request):
    llanguage = Language.objects.all()
    if request.user.is_superuser:
        context = {
            'llanguage': llanguage
        }
        return render(request, 'language/list.html', context=context)
    else:
        return redirect('login')

def addLanguage(request):
    if request.POST:
        staticF = LanguageForm(request.POST, request.FILES)
        if staticF.is_valid():
            staticF.save()
    if request.user.is_superuser:
        staticF = LanguageForm()
        context = {
            'formLanguage': staticF
        }
        return render(request, 'language/add.html', context=context)
    else:
        return redirect('login')
    
def deleteLanguage(request, pk):
    dlanguage = Language.objects.get(pk=pk)
    if request.user.is_superuser:
        dlanguage.delete()
        return listLanguage(request)
    else:
        return redirect('login')