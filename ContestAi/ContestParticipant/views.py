from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# import random
# from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
        #update Profile
    if request.method == 'POST':
        print("Update Profile comming soon")
        return
        

    haveError = False
        #Select Database
    try:
        conn = sqlite3.connect('./db.sqlite3')

        cmd = 'SELECT * FROM ContestAdmin_account'
        contestSubmited = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_account'
        contestRegisted = conn.execute(cmd)
        
        cmd = 'SELECT * FROM ContestAdmin_account'
        contestAll = conn.execute(cmd)
    except EOFError as e:
        print(e)
        haveError = True


    
        #Render Site
    dic = {'haveError': haveError, 'contestSubmited': contestSubmited, 'contestRegisted': contestRegisted, 'contestAll': contestAll}
    return render(request, 'ContestParticipant/index.html', dic)




def error(request):
    return render(request, 'ContestParticipant/error.html')