from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def mainvid(request):
    return render(request, 'authentication/mainvid.html')

@login_required
def afterlogin(request):
    return render(request, 'authentication/afterlogin.html')

def history(request):
    return render(request, 'authentication/history.html')

def favorites(request):
    return render(request, 'authentication/favorites.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('mainvid')
    else:
        form = UserRegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid() :
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'authentication/profile.html', context)
