from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_anonymous:
        if request.method == 'GET':
            return render(request, 'main/home.html', \
            {'form':AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'],\
            password=request.POST['password'])
            if user is None:
                return render(request, 'main/home.html', \
                {'form':AuthenticationForm(),'error': 'User and password did not match'})
            login(request,user)
            return redirect('apps')
    else:
        return redirect('apps')

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def signup_user(request):
    if request.user.is_anonymous:
        if request.method == 'GET':
            form = UserCreationForm()
            form.fields['username'].help_text=""
            form.fields['password1'].help_text=""
            form.fields['password2'].help_text=""
            return render(request, 'main/signupuser.html', \
            {'form': form})
        else:
            if request.POST['password1']==request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'],\
                    password = request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('apps')
                except IntegrityError:
                    return render(request,'main/signupuser.html',\
                    {'form':UserCreationForm,'error':'That username as already been taken!'})
            else:
                return render(request,'main/signupuser.html',\
                {'form':UserCreationForm,'error':'Password did not match!'})
    else:
        return redirect('apps')

@login_required
def apps(request):
    return render(request, 'main/apps.html')