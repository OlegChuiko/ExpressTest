from users.forms import UserLoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as user_logout
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from dashboard.views import dashboard
from django.contrib import auth
from django.urls import reverse


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashBoard')

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request,username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('dashboard:dashBoard'))
    else:
        form = UserLoginForm()
    return render(request,'main/login.html',{'form': form})

@login_required()
def logout(request):
    user_logout(request)
    return redirect('main:index')



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Присвоюємо значення email полю username
            user.save()
            return HttpResponseRedirect(reverse('dashboard:dashBoard'))
    else:
        form = UserRegistrationForm()
    return render(request,'main/registration.html',{'form':form})