from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone= forms.CharField(max_length=10,required=True)
    employee_id = forms.CharField(max_length=30, required=True)
    designation = forms.CharField(max_length=30, required=True)
    number_of_leaves= forms.CharField(max_length=2,required=True)
    department_number= forms.CharField(required=True)
    address = forms.CharField(max_length=200, required=True)
  

    class Meta:
        model=User
        fields=['employee_id','password1','password2','username','department_number','designation','email','phone','address','number_of_leaves']