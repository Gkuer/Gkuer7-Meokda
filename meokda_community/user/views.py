from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import meokda_user
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm
from django.views.generic import ListView, DeleteView, DetailView,CreateView,UpdateView 


# Create your views here.

def index(request):
    return render(request, 'base.html', {'username': request.session.get('user')})

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        return redirect('/')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.username
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form': form})



def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username", None)
        useremail = request.POST.get("useremail", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re-password", None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        
        else:
                
            meokdauser = meokda_user(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

            meokdauser.save()
            
            return redirect('/user/login')
        return render(request, 'register.html', res_data)

def about(request):
    return render(request, 'about.html')

class UserProfile(DetailView):
    template_name = "UserProfile.html"
    queryset = meokda_user.objects.all()
    context_object_name = 'uuser'