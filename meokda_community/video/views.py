from django.db.models.query_utils import select_related_descend
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import Video
from .forms import VideoForm
from django.views.generic import ListView, DeleteView, DetailView,CreateView,UpdateView 
from user.models import meokda_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from user.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import geocoder


from django.template import loader
import urllib.request
import ssl
import json
from django.http import JsonResponse

# 메인화면
class VideoListView(ListView):
    model = Video
    paginate_by = 4
    context_object_name = 'video_list'
    template_name = 'video/video_list.html'

    
    def get_context_data(self, **kwargs):
        g= geocoder.ip('me')
        # Call the base implementation first to get the context
        context = super(VideoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['ddd'] = meokda_user.objects.filter(username=self.request.session.get('user'))
        context['mylat'] = g.lat
        context['mylng'] = g.lng
        return context
    
    def get_ordering(self):
        g = geocoder.ip('me')
        vix = Video.objects.all

        ordering = self.request.GET.get('ordering',vix)

# 비디오 업로드

@method_decorator(login_required, name='dispatch')
class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'form2.html'

    def get_context_data(self, **kwargs):
        context = super(VideoCreateView, self).get_context_data(**kwargs)
        context['ddd'] = meokda_user.objects.filter(username=self.request.session.get('user'))
        context['video'] = Video.objects.all()
        return context
        
    def form_valid(self, form):
        video = form.save(commit=False)
        user_id = self.request.session.get('user')
        meokdauser = meokda_user.objects.get(username = user_id)
        video.author = meokdauser
        return super().form_valid(form)
    
@method_decorator(csrf_exempt)
def Search_try(request):
    if request.is_ajax():
        data = request.GET.get('keyinput')
        context = ssl._create_unverified_context()
        client_id = "qEhfLhkgPu7mnd2RR706"
        client_secret = "uE9Ci84q6C"
        inputText = data
        encText = urllib.parse.quote(inputText)
        url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=5&start=1&sort=random" # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request2 = urllib.request.Request(url)
        request2.add_header("X-Naver-Client-Id",client_id)
        request2.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request2,context=context)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            ddd = json.loads(response_body.decode('utf-8'))
            items = ddd.get('items')
            restaurant = ""

            for i in items:
                restaurant += "," + i['title']
                address = i['address']
                mapx = i['mapx']
                mapy = i['mapy']

            restaurant = restaurant.replace("</b>","")
            restaurant = restaurant.replace("<b>","")
            address = address.replace("</b>","")
            address = address.replace("<b>","")
            mapx = mapx.replace("</b>","")
            mapx = mapx.replace("<b>","")
            mapy = mapy.replace("</b>","")
            mapy = mapy.replace("<b>","")
            


            context = {
                'restaurant' : restaurant,
                'address' : address,
                'mapx' : mapx,
                'mapy' : mapy

            }

            return JsonResponse(context,status=200)

        else:
            ddd= "Error Code:" + rescode
            return JsonResponse(context,status=200)

    return render(request, 'form2.html')

class VideoDetailView(DetailView):
    model = Video


class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'


class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video:video_list')



# 다른 사람이 보는 프로필
def UserProfile(request, username2):
    babo = Video.objects.filter(author = meokda_user.objects.get(username = username2))
    babo2 = username2
    babo3 = meokda_user.objects.get(username = username2)
    return render(request,'UserProfile.html',{'babo':babo, 'babo2':babo2, 'babo3':babo3})

# Search Test


@csrf_exempt
def SearchTest(request):
    return render(request, 'search_test.html')