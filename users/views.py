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
            render(request,'users/profile.html')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
def home(request):
    if (request.method)=="POST":
        HODNAME=request.POST['Username']
        PASS =request.POST['pwd']
        det = { "HODNAME":HODNAME,"PASS":PASS}
        token = requests.post("https://cosc-team-14-restapi.herokuapp.com/hod_login",det)
        '''token=token.json()['access_token']
        data=requests.get("https://cosc-team-14-restapi.herokuapp.com/hod_register",headers={'Authorization':'Bearer{}'.format(token)},data={'routeId':48})
        return HttpResponse(data)'''
        global p
        p = token.json()
        #return render(request,'users/profile.html',{'users':p})
        if(len(p)!=2):
              messages.success(request,f'Invalid Credentials')
              return render(request,'users/login.html')
            #return HttpResponse(p)
        else:
            global t
            global q
            t=token.json()[" access_token "]
            q = token.json()["hodname"]
            return render(request,'users/profile.html',{'users':t})
        '''else:
            data=requests.get("https://cosc-team-14-restapi.herokuapp.com/hod_register",headers={'Authorization':f'Bearer{p}'})
             
            res = data.json()
            context={'data': res,}
            return redirect('home')'''
        '''elif (request.method)=="GET":
        if(p):
            if(p=="Invalid credentials"):
                print('invalid')
                context={'data':"INVALID CREDENTIALS"}
                return render(request,'login1.html',context)
            #return HttpResponse(p)
            else:'''
        



def profile(request):
    #onclick="myFunction()"
    #token=token.json()['access_token']
    #data=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',headers={'Authorization':'Bearer{}'.format(token)},data={'routeId':48})

    #print(data.json)
    #return render(request,'users/profile.html',{'data':t})
    if(t!=''):
        data={"HODNAME":q}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/hod_register',data,headers={'Authorization':f'Bearer {t}'})
        res=resp.json()
        return render(request,'users/profile.html',{'users':t,'details':res})
    else:
        return redirect('login')
def index(request):
    data=request.GET.get('id')

    return HttpResponse(data)

def about1(request):
    x=request.GET.get("checkhistory")
    y=request.GET.get("leave_id")
    if(x!=None):
        data={"EMPID":x}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/emp_register',data,headers={'Authorization':f'Bearer {t}'})
        ro=resp.json()
        return render(request,'users/about1.html',{'values':ro,"leave_id":y})
    else:
        return render(request, 'users/about1.html',{'title':'About'})
    '''if(p!=''):
       return render(request, 'users/about1.html',{'title':'About','users':p})
    else:
        return redirect('login')'''
    
    
def applyleave(request):
    
    if(t!=''):
       return render(request,'blog/applyleave.html',{'users':t})
    else:
        return redirect('login')
    

def table1(request):
    '''resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/empleave',headers={'Authorization':f'Bearer {t}'})
    ro=resp.json()
    return render(request,'users/table1.html',{'values':ro})'''
    #return render(request,'users/table1.html')
    x=request.GET.get("checkhistory")
    
    if(x!=None):
        data={"DEPTNO":x}
        resp=requests.get('https://cosc-team-14-restapi.herokuapp.com/empleave',data,headers={'Authorization':f'Bearer {t}'})
        ro=resp.json()
        return render(request,'users/table1.html',{'values':ro})
    else:
        return render(request, 'users/table1.html')
    '''if(p!=''):
       return render(request, 'users/about1.html',{'title':'About','users':p})'''
    
def home3(request):
    LEAVE_MSG=request.GET.get("LEAVE_MSG")
    LEAVE_ID=request.GET.get("LEAVE_ID")
    LEAVE_STAT=request.GET.get("LEAVE_STAT")
    data={"LEAVE_MSG":LEAVE_MSG,"LEAVE_ID":LEAVE_ID,"LEAVE_STAT":LEAVE_STAT}
    resp=requests.post('https://cosc-team-14-restapi.herokuapp.com/leaveapproval',data,headers={'Authorization':f'Bearer {t}'})
    return HttpResponse(resp.text)


   

def calendar1(request):
    return render(request,'users/calendar1.html')

