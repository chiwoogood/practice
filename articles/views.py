from django.shortcuts import render

# Create your views here.
def index(request):
    #환영하는 메인 페이지를 보여준다.
    context ={
        'name' : 'janggoo',
        'age' : 28
    }
    return render(request,'articles/index.html',context)

def welcome(request, name):
    # 사람들이 /welcom/본인이름을 입력하면 환영 인사와 이름을 동시에 보여준다.
    context = {
        'name' : name
    }
    return render(request,'articles/welcome.html',context)

def fakelove(request):
    

    return render(request,'articles/fakelove.html')

def ping(request):

    return render(request,'articles/ping.html')

def pong(request):
    name = request.GET.get('ball')
    context = {
        'name' : name
    }
    return render(request,'articles/pong.html',context)