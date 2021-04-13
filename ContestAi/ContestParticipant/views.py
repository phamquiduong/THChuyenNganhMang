from django.shortcuts import render
from django.http import HttpResponse
import random
from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
    if request.method == 'POST':
        upload_file = request.FILES['submit_file']
        print(upload_file.name)
        print(upload_file.size)
        upload_file.save()
        i = random.randint(0, 1000000)






    # title = 'Đây là cái tiêu đề'
    # link_pdf = 'https://vinasupport.com/my_pdf_file.pdf'
    # luu_y = ['1, ABC', '2, XYZ']
    # dic = {'title': title, 'link_pdf': link_pdf, 'luu_y': luu_y}
    return render(request, 'ContestParticipant/index.html')
