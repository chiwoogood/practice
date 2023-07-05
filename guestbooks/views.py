from django.shortcuts import render
from .models import Guestbook

def index(request):
    guestbook = Guestbook.objects.all()
    context = {
        'guestbook' : guestbook,
    }
    return render(request,'guestbooks/index.html',context)

def create(request):
    content = request.POST.get('content')
    context ={
        'content' : content,
    }
    Guestbook.objects.create(content=content)

    return render(request,'guestbooks/create.html',context)
# Create your views here.
