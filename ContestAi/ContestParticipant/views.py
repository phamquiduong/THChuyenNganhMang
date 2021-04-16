from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session


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