from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


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
    return render(request,'blog/table.html')



