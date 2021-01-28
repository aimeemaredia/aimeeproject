#    Aimee Maredia 
#    Mr. Moore
#    ICS4U 
#    Jan 29,2019
#    views.py file to save the register and profile forms and to redirect the user to those pages 

#imports 
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

#method to get register form input and to save it. 
def register(request):
    # if the POST method is activated then save a local instance of the userRegistration form 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #if the form is valid then save it 
        if form.is_valid():
            form.save()
            #get a string of the username 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login! ')
            #redirect to the login page 
            return redirect('login')
    #if the form is not valid then take user back to the register page 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#method to update the user information and profile picture 
@login_required
def profile(request):
    # if the POST method is activated then save a local instance of the userUpdateFrom and ProfileUpdateFrom
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #if the forms are valid then save it 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated! ')
            #redirect to the profile page 
            return redirect('profile')
            
    #if the form is not valid then take user back to the register page
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
