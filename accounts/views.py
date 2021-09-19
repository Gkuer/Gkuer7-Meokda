from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.models import User
# Create your views here.

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'videos:main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_http_methods(["GET","POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
        return redirect("videos:main")

    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect('accounts:login')

@require_http_methods(["GET","POST"])
def profile(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        pass
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

@require_safe
def about(request):
    return render(request,'accounts/about.html')