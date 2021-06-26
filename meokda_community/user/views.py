from video.models import Video
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import meokda_user
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm,ImageForm
from django.views.generic import ListView, DeleteView, DetailView,CreateView,UpdateView 
import calendar


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


# 프로필 뷰
def image(request,username):
    # 역참조
    icecream = meokda_user.objects.get(username = request.session.get('user'))
    icecream2 = icecream.video_set.all()

    # test
    boby = Video.objects.all()
    # meta 포함된 login_user 인자 가져오기
    user2 = meokda_user.objects.get(username = request.session.get('user'))

    #instance적용시키고 이미지폼 불러오기
    form = ImageForm(instance=user2)
    # Video_list = Video
    #해당 유저만 자기 프로필 접속할수 있도록 user2 설정
    username2 = request.session.get('user')



    if username == username2:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES, instance= user2)
            if form.is_valid():
                form.save()
        return render(request,'profile.html',{'okky':user2, 'form':form, 'git':icecream2, 'bob':boby})

    else:
        return redirect('http://127.0.0.1:8000/user/login/')
