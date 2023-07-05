from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboards:create')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/signup.html',context)

def detail(request,pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user' :user
    }
    return render(request,'accounts/detail.html',context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())            
            return redirect(request.GET.get('next') or 'dashboards:new')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('dashboards:new')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()           
            return redirect('accounts:detail',request.user.pk)
    else:
        form = CustomUserChangeForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)       
            return redirect('dashboards:new')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request,'accounts/passwordChange.html',context)


def delete(request):
    request.user.delete()
    auth_logout(request) 
    return redirect('dashboards:new')