from django.shortcuts import render
from django.shortcuts import render,redirect
#from .forms import EmployeeModelForm
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import EmployeeModel
from .forms import SignupForm, EmployeeModelForm, AdminModelForm, form_status


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
            print(type(uname))
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                print("------")
                return HttpResponseRedirect('/ticket')
        elif str(request.POST['username']) == 'admin' and str(request.POST['password']) == 'admin':
            return HttpResponseRedirect('/adminpage')
   else:
        fm = AuthenticationForm()
   return render(request, 'user_login.html', {'form': fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# def ticket_rise(request):
#     if request.method == "POST":
#         fm = EmployeeModelForm(request.POST)
#         if fm.is_valid():
#             qu = fm.cleaned_data['Query']
#             obj = EmployeeModel(Query=qu,username=request.user)
#             obj.save()
#     else:
#         fm = EmployeeModelForm()
#     st = EmployeeModel.objects.all()
#     return render(request,"ticket.html",{'tform':fm,"statu":st})

def ticket_rise(request):
    if request.method == "POST":
        fm = EmployeeModelForm(request.POST)
        if fm.is_valid():
            qu = fm.cleaned_data['Query']
            print(request.user)
            obj = EmployeeModel(Query=qu,username=request.user)
            obj.save()
    else:
        fm = EmployeeModelForm()
    if request.user == 'admin':
        det = EmployeeModel.objects.all()
    else:
        # det = EmployeeModel.objects.all().filter(username=request.user)
        # print(det)
        to = EmployeeModel.objects.all()
        lst = {}
        for i in to:
            if str(i.username) == str(request.user):
                print(i.username)
                lst['username']=i.username
                lst['query']=i.Query
                lst['status']=i.status
        print(lst)
    return render(request,"ticket.html",{'tform':fm,"details":lst,"user":request.user,"admin":"admin"})

def adminpage(request):
    form = EmployeeModel.objects.all()
    return render(request,"admin.html",{'total':form})

def update(request,id):
    if request.method == 'POST':
        stu = EmployeeModel.objects.get(pk=id)
        form = form_status(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'successfully updated!')
            return HttpResponseRedirect('/adminpage')
    else:
        stu = EmployeeModel.objects.get(pk=id)
        form = form_status(instance=stu)
    return render(request, 'update.html', {'form': form})
