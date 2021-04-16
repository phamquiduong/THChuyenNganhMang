from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.

def clean(x):
    uni = ('à','á','ả','ã','ạ','â','ầ','ấ','ẩ','ẫ','ậ','ă','ằ','ắ','ẳ','ẵ','ặ','è','é','ẻ','ẽ','ẹ','ê','ề','ế','ể','ễ','ệ','đ','ì','í','ỉ','ĩ','ị','ò','ó','ỏ','õ','ọ','ô','ồ','ố','ổ','ỗ','ộ','ơ','ờ','ớ','ở','ỡ','ợ','ù','ú','ủ','ũ','ụ','ư','ừ','ứ','ử','ữ','ự','ỳ','ý','ỷ','ỹ')
    t = ''
    for c in x:
        if ('a'<=c and c<='z') or ('A'<=c and c<='Z') or ('0'<=c and c<='9') or (c=='@') or (c in uni): t+=c
    return t

def index(request):
        #Bằng 1 cách thần kỳ nào đó lấy trong cái gì đó.. Có được ID
    id = '2'
    haveError = False


        #Proc
    if request.method == 'POST':

        if request.POST.get('feature')=='2':
                #Remove Registed
            iDcontest = clean(request.POST.get('idContest'))
            idUser = clean(request.POST.get('idUser'))
            try:
                conn = sqlite3.connect('./db.sqlite3')
                cmd = "DELETE FROM ContestAdmin_registercontest WHERE IDcontest='{}' AND IDUser='{}'".format(iDcontest,idUser)
                print(cmd)
                conn.execute(cmd)
                conn.commit()
            except EOFError as e:
                print(e)
                haveError = True
    
        if request.POST.get('feature')=='3':
                #Remove Registed
            iDcontest = clean(request.POST.get('idContest'))
            idUser = clean(request.POST.get('idUser'))
            try:
                conn = sqlite3.connect('./db.sqlite3')
                cmd = "INSERT INTO ContestAdmin_registercontest(IDcontest,IDUser) VALUES ('{}','{}')".format(iDcontest,idUser)
                conn.execute(cmd)
                conn.commit()
            except EOFError as e:
                print(e)
                haveError = True

        if request.POST.get('feature')=='4':
            userName = clean(request.POST.get('userName'))
            lastName = clean(request.POST.get('lastName'))
            firstName = clean(request.POST.get('firstName'))
            email = clean(request.POST.get('email'))
            newPass = clean(request.POST.get('newPass'))
            idUser = clean(request.POST.get('idUser'))

            if (userName!='' and lastName!='' and firstName!='' and email!=''):
                try:
                    conn = sqlite3.connect('./db.sqlite3')
                    cmd = "UPDATE auth_user SET username='{}', last_name='{}', email='{}', first_name='{}' WHERE id='{}'".format(userName,lastName,email,firstName,idUser)
                    conn.execute(cmd)
                    conn.commit()
                except EOFError as e:
                    print(e)
                    haveError = True
            
            if (newPass!=''):
                try:
                    conn = sqlite3.connect('./db.sqlite3')
                    cmd = "UPDATE auth_user SET password=MD5('{}') WHERE id='{}'".format(newPass,idUser)
                    conn.execute(cmd)
                    conn.commit()
                except EOFError as e:
                    print(e)
                    haveError = True

            


    
        #Select Database
    try:
        conn = sqlite3.connect('./db.sqlite3')

        cmd = "SELECT * FROM ContestAdmin_status JOIN ContestAdmin_contest ON ContestAdmin_status.IDcontest = ContestAdmin_contest.id JOIN ContestAdmin_language ON ContestAdmin_language.id = ContestAdmin_contest.IDLanguage WHERE ContestAdmin_status.IDUser = '{0}'".format(id)
        contestSubmited = conn.execute(cmd)
        
        cmd = "SELECT * FROM ContestAdmin_registercontest JOIN ContestAdmin_contest ON ContestAdmin_contest.id = ContestAdmin_registercontest.IDContest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_registercontest.IDUser='{0}' AND ContestAdmin_registercontest.IDcontest NOT IN (SELECT (IDcontest) FROM ContestAdmin_status WHERE IDUser = '{0}')".format(id)
        contestRegisted = conn.execute(cmd)
        
        cmd = "SELECT * FROM ContestAdmin_contest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_contest.id NOT IN (SELECT (IDcontest) FROM ContestAdmin_registercontest WHERE ContestAdmin_registercontest.IDUser = '{0}')".format(id)
        contestAll = conn.execute(cmd)

        cmd = "SELECT username, last_name, first_name, email FROM auth_user WHERE id='{0}'".format(id)
        for row in conn.execute(cmd):
            infoUser = row

    except EOFError as e:
        print(e)
        haveError = True

        #Render Site
    dic = {'id': id, 'infoUser': infoUser, 'haveError': haveError, 'contestSubmited': contestSubmited, 'contestRegisted': contestRegisted, 'contestAll': contestAll}
    return render(request, 'ContestParticipant/index.html', dic)


class ParticipantView(View):
    def get(self, request):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context = {
                'name': userName,
                'listContext':[],
            }
            return render(request, path.templateParticipant , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('login')
    def post(self, request):
        #do sth
        return redirect('./')
