from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request, ):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['user_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, try again')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout was successful')
    return redirect('home')