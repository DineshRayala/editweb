from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            HODID=request.POST['HODID']
            PASS=request.POST['PASS']
            r=requests.post('skillup-team-14.cxgok3weok8n.ap-south-1.rds.amazonaws.com/hod_register',data={'HODID':HODID,'PASS':PASS})
            p=r.json()['message']
            if p=="ALLOW ACCESS !!":
                return render(request,'users/login.html')
            else :
                content={"message":"Invalid Credentials"}
                return render(request,'users/login.html',content)
            
            
            #messages.success(request, f'Your account has been created! You are now able to log in')
            #return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

def index(request):
    data="Hello world"
    context={'message':data}
    return render (request,'users/index.html',context)



