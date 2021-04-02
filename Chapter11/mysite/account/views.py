from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserCreationForm
from .forms import UserRegistrationForm, UserRegistrationForm2
from django.contrib.auth import forms as auth_forms

def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'account/profile.html', {'user':user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('OK')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup_form.html', {'form':form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html', {'user_form': user_form})


def register2(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm2(request.POST, request.FILES)
        if user_form.is_valid():
            new_user=user_form.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm2()
    return render(request,'account/register.html', {'user_form': user_form}) 



from django.contrib.auth.decorators import login_required

@login_required
def user_detail(request):
    return render(request, 'registration/detail.html')

