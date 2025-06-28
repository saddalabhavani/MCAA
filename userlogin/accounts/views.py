from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        User.objects.create(username=uname, email=email, password=pwd)
        messages.success(request, 'Registration successful.')
        return redirect('login')
    
    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')


def user_logout(request):
    request.session.flush()
    return redirect('login')



