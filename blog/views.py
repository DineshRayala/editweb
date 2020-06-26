from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
import requests
import json
# Create your views here.

def index(request):
    return render(request,'blog/calendar. html')
    
def info(request):
    response=requests.get('https://skillup-team-14.cxgok3weok8n.ap-south-1.rds.amazonaws.com')
    info=response.json()
    return render(request, 'blog/info.html',info)
  

def home(request):
    context={
        'posts':Post.objects.all()
    }
   
    
    return render(request, 'blog/home.html',context)

@login_required
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
    
def applyleave(request):
    return render(request,'blog/applyleave.html')

def table(request):
    r=requests.get('https://cosc-team-14-restapi.herokuapp.com/empleave')
    t=r.json()
    return render(request,'blog/table.html',{'data':t})



