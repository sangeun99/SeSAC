from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

@login_required
def home_view(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request, 'helloworldapp/home.html', context=context)

def login_view(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print("로그인에 성공하였습니다")
            login(request, user)
            return redirect('home')
        else : 
            
            return "로그인에 실패하였습니다"
    return render(request, 'helloworldapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')