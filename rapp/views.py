from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UsrRegForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import views as auth_views


# Create your views here.
def register(request):
    if request.method == 'POST':
        usr_reg_form = UsrRegForm(request.POST)
        if usr_reg_form.is_valid():
            usr_reg_form.save()
            username = usr_reg_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now login!')
            return redirect('yapp-home')
    else:    
        usr_reg_form = UsrRegForm()
    return render(request, 'rapp/register.html', {'yform': usr_reg_form} )

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Google for 'post get redirect pattern'
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'rapp/profile.html', context)