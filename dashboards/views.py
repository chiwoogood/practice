from django.shortcuts import render, redirect
from .models import Dashboard
from .forms import DashboardForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# def index(request):
#     dashboardForm = DashboardForm()
#     context ={
#         'dashboardForm' : dashboardForm
#     }
#     return render(request,'dashboards/index.html',context)

@login_required
def create(request):  
    if request.method =='POST':
        dashboardForm = DashboardForm(request.POST,request.FILES)
        if dashboardForm.is_valid():
            dashboardForm.save()
            messages.success(request, '게시글을 작성하였습니다.')
            return redirect('dashboards:new')
    else:
        dashboardForm = DashboardForm()
    context = {
        'dashboardForm' : dashboardForm
    }
    return render(request,'dashboards/index.html',context)
    
    

def new(request):
    dashboards = Dashboard.objects.order_by('title')
    context ={
        'dashboards' : dashboards
    }
    return render(request,'dashboards/new.html',context)

def detail(request,pk):
    dashboards = Dashboard.objects.get(pk=pk)
    context = {
        'dashboards' : dashboards
    }
    return render(request,'dashboards/detail.html',context)

@login_required
def update(request,pk):
    dashboard = Dashboard.objects.get(pk=pk)
    if request.method =='POST':
        dashboardForm = DashboardForm(request.POST,instance=dashboard)
        if dashboardForm.is_valid():
            dashboardForm.save()
            return redirect('dashboards:new')
    else:
           dashboardForm = DashboardForm(instance=dashboard)
    context= {
        'dashboardForm' : dashboardForm
    }
    return render(request,'dashboards/update.html',context)

def delete(request,pk):
    dashboard = Dashboard.objects.get(pk=pk)
    dashboard.delete()
    return redirect('dashboards:new')