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
def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
@login_required
def applyleave(request):
    return render(request,'blog/applyleave.html')