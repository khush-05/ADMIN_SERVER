from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages  # For error messages
from django.db import connection

def Admin_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('Admin_login')  # ✅ Correct redirect
        else:
            messages.error(request, "Invalid registration details.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'Admin_register.html', {'form': form})

def Admin_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Admin_home')  # ✅ Correct redirect
            else:
                form.add_error(None, "Invalid login credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'Admin_login.html', {'form': form})


def Admin_home(request):
    return render(request , 'Admin_home.html')  

def Option1(request):
    return render(request , 'Option1.html')

def Option2(request):
    return render(request , 'Option2.html')

def Option3(request):
    return render(request , 'Option3.html')

def Option4(request):
    return render(request , 'Option4.html')



