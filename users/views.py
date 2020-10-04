from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRrgisterForm , UserProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRrgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRrgisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')
    else:
        form = UserProfileForm(instance=profile)
    return render(request,'users/profile.html',{'form':form})