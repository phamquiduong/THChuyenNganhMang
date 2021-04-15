from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# import random
# from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
        #Bằng 1 cách thần kỳ nào đó lấy trong cái gì đó.. Có được ID
    id = '2'
    haveError = False


        #Proc
    if request.method == 'POST':
        if request.POST.get('feature')=='2':
                #Remove Registed
            iDcontest = request.POST.get('idContest')
            idUser = request.POST.get('idUser')
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
            iDcontest = request.POST.get('idContest')
            idUser = request.POST.get('idUser')
            try:
                conn = sqlite3.connect('./db.sqlite3')
                cmd = "INSERT INTO ContestAdmin_registercontest(IDcontest,IDUser) VALUES ('{}','{}')".format(iDcontest,idUser)
                conn.execute(cmd)
                conn.commit()
            except EOFError as e:
                print(e)
                haveError = True

        if request.POST.get('feature')=='4':
            userName = request.POST.get('userName')
            lastName = request.POST.get('lastName')
            firstName = request.POST.get('firstName')
            email = request.POST.get('email')
            newPass = request.POST.get('newPass')
            idUser = request.POST.get('idUser')

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