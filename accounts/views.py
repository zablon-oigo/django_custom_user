from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm,LoginForm
from django.contrib.auth.decorators import login_required
def sign_in(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,email=email, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            return render(request,'aaccounts/register_done.html',{'user':user})
    else:
        form=CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
            

