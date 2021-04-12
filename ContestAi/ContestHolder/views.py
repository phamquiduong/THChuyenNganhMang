from django.shortcuts import render,redirect
from django.views import View
from django import template
from service import path,session


mockData = [{
  "idContest": "5664c5c9-a3ff-4093-b734-d66c234e46ff",
  "title": "Revolt of the Zombies",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget accumsan risus. Morbi congue consectetur vulputate. Cras sed est sagittis, gravida risus ut, dictum leo. Quisque tristique risus elit, ac blandit magna faucibus sit amet. Ut sed ligula a tortor sagittis aliquam. Aenean nec tellus in mi fermentum aliquam eu ut turpis. ",
  "timeRegister": "12/25/2020",
  "timeStart": "10/4/2020",
  "timeEnd": "4/7/2021",
  "language": "Malayalam"
}, {
  "idContest": "1616b720-61fb-4265-a693-2d2c87b5d661",
  "title": "Bill Burr: I'm Sorry You Feel That Way",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget accumsan risus. Morbi congue consectetur vulputate. Cras sed est sagittis, gravida risus ut, dictum leo. Quisque tristique risus elit, ac blandit magna faucibus sit amet. Ut sed ligula a tortor sagittis aliquam. Aenean nec tellus in mi fermentum aliquam eu ut turpis. ",
  "timeRegister": "4/8/2020",
  "timeStart": "1/2/2021",
  "timeEnd": "8/15/2020",
  "language": "Romanian"
}, {
  "idContest": "cc60495e-51fd-4497-97c9-27f732f225f7",
  "title": "The Flower in His Mouth",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget accumsan risus. Morbi congue consectetur vulputate. Cras sed est sagittis, gravida risus ut, dictum leo. Quisque tristique risus elit, ac blandit magna faucibus sit amet. Ut sed ligula a tortor sagittis aliquam. Aenean nec tellus in mi fermentum aliquam eu ut turpis. ",
  "timeRegister": "5/10/2020",
  "timeStart": "2/26/2021",
  "timeEnd": "5/24/2020",
  "language": "Estonian"
}, {
  "idContest": "e79da123-32b6-48f6-b9f2-aa41d260262b",
  "title": "More Than Honey",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget accumsan risus. Morbi congue consectetur vulputate. Cras sed est sagittis, gravida risus ut, dictum leo. Quisque tristique risus elit, ac blandit magna faucibus sit amet. Ut sed ligula a tortor sagittis aliquam. Aenean nec tellus in mi fermentum aliquam eu ut turpis. ",
  "timeRegister": "12/29/2020",
  "timeStart": "8/18/2020",
  "timeEnd": "11/19/2020",
  "language": "Kannada"
}, {
  "idContest": "667589e8-6937-45d9-8d78-9c1914595aec",
  "title": "Heart of a Lion",
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget accumsan risus. Morbi congue consectetur vulputate. Cras sed est sagittis, gravida risus ut, dictum leo. Quisque tristique risus elit, ac blandit magna faucibus sit amet. Ut sed ligula a tortor sagittis aliquam. Aenean nec tellus in mi fermentum aliquam eu ut turpis. ",
  "timeRegister": "12/17/2020",
  "timeStart": "3/4/2021",
  "timeEnd": "9/9/2020",
  "language": "Bosnian"
}]

class HolderView(View):
    def get(self, request):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            context = {
                'name': userName,
                'dataContests': mockData,
            }
            return render(request, path.templateHolder , context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('../login')
class ContestDetail(View):
    def get(self, request,id):
        if session.isAuthenticated(request):
            userName = str()
            try:
                userName = request.session.get('user')['name']
            except:
                userName = ''
            detailData = filter(lambda x: id == x['idContest'], mockData)
            context = {
                'name': userName,
                'dataContests': detailData,
                'linkContest': 'demo/Contest1.pdf',
                'linkDataTrain': 'demo/test1.txt',
                'inRegis': 80,
                'inTodo': 53,
                'inResult':69
            }
            return render(request, path.templateDetail, context)
        else:
            request.session['messAuth'] = 'Please Log In'
            return redirect('../login')

      