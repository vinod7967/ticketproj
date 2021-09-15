from django.shortcuts import render
from django.shortcuts import render,redirect
#from .forms import EmployeeModelForm
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import EmployeeModel, AdminModel
from .forms import SignupForm, EmployeeModelForm, AdminModelForm


def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Succesfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})
def user_login(request):
   global uname
   ''' if not request.user.is_authenticated:'''
   if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        print(request.POST['username'],request.POST['password'])
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/ticket')
        elif str(request.POST['username']) == 'admin' and str(request.POST['password']) == 'admin':
            return HttpResponseRedirect('/adminpage')
   else:
        fm = AuthenticationForm()
   return render(request, 'user_login.html', {'form': fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def ticket_rise(request):
    if request.method == "POST":
        fm = EmployeeModelForm(request.POST)
        if fm.is_valid():
            qu = fm.cleaned_data['Query']
            obj = EmployeeModel(Query=qu,username=uname)
            obj.save()
    else:
        fm = EmployeeModelForm()
    det = EmployeeModel.objects.select_related('adminmodel').get(username=uname)
    st = AdminModel.objects.all()
    print(det)
    return render(request,"ticket.html",{'tform':fm,"details":det,"statu":st})
def adminpage(request):
    if request.method == "POST":
        fm = AdminModelForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = AdminModelForm()
    tot = AdminModel.objects.all()
    return render(request,"admin.html",{"aform":fm,'total':tot})