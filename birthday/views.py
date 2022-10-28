from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, 'birthday/index.html',{
        'is_birthday': now.month == 11 and now.day == 8
    })