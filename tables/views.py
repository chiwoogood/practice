from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm
# Create your views here.
def create(request):
    if request.method=="POST":
        tableForm = TableForm(request.POST)
        if tableForm.is_valid():
            tableForm.save()
            return redirect('tables:list')
    else:
        tableForm = TableForm()
    context ={
        'tableForm' : tableForm
    }
    return render(request,'tables/index.html',context)

def list(request):
    tables = Table.objects.all()
    context ={
        'tables' : tables
    }
    return render(request,'tables/list.html',context)

def detail(request,pk):
    tables = Table.objects.get(pk=pk)
    context={
        'table' :tables
    }
    return render(request,'tables/detail.html',context)