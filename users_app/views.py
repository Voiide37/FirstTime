from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('New User Account Created!. Login to get started'))
            return redirect('login')
        
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'register.html', {'register_form': register_form})
    else:       
        register_form = CustomRegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
