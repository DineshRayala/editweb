from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import requests
import json

from django.http import HttpResponse,JsonResponse
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            data=request.POST.copy()
            HODID =int(form.cleaned_data.get('hod_id'))
            HODNAME=str(form.cleaned_data.get('username')) 
            DEPTNO =int(form.cleaned_data.get('department_number'))
            DESG =str(form.cleaned_data.get('designation'))
            EMAIL =str(form.cleaned_data.get('email'))
            CONTACT=str(form.cleaned_data.get('phone')) 
            ADDRESS =str(form.cleaned_data.get('address'))
            PASS =str(form.cleaned_data.get('password1'))
            data={"HODID":HODID,"HODNAME":HODNAME,"DEPTNO":DEPTNO,"DESG":DESG,"EMAIL":EMAIL,"CONTACT":CONTACT,"ADDRESS":ADDRESS,"PASS":PASS}
            resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/hod_register',data)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return HttpResponse(resp.text)
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
def home(request):
    if (request.method)=="POST":
        HODNAME=request.POST['Username']
        PASS =request.POST['pwd']
        det = { "HODNAME":HODNAME,"PASS":PASS}
        token = requests.post("https://cosc-team-14-restapi.herokuapp.com/hod_login",det)
        global p
        p = token.json()
        
        if(p['message']=="Invalid credentials"):
            context={'data':"INVALID CREDENTIALS"}
            return render(request,'login.html',context)
            #return HttpResponse(p)
        '''else:
            data = requests.get("https://sport-resources-booking-api.herokuapp.com/ResourcesPresent", headers = {'Authorization':f'Bearer {p}'}) 
            res = data.json()
            context={'data': res,}
            return redirect('resources')'''
        '''elif (request.method)=="GET":
        if(p):
            if(p=="Invalid credentials"):
                print('invalid')
                context={'data':"INVALID CREDENTIALS"}
                return render(request,'login1.html',context)
            #return HttpResponse(p)
            else:'''
        

@login_required

def profile(request):
    #token=requests.post('https://cosc-team-14-restapi.herokuapp.com/login',data={'HODID':HODID,'PASS':PASS})
    #token=token.json()['access_token']
    #data=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',headers={'Authorization':'Bearer{}'.format(token)},data={'routeId':48})

    #print(data.json)
    #return render(request,'users/profile.html',{'data':t})
    return render(request,'users/profile.html')

def index(request):
    data="Hello world"
    context={'message':data}
    return render (request,'users/index.html',context)



