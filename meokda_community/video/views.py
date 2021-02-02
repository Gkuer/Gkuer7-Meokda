from django.db.models.query_utils import select_related_descend
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.views.generic import ListView, DeleteView, DetailView,CreateView,UpdateView 
from user.models import meokda_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# import simplejson as json
# from rest_framework import generics
# from rest_framework.pagination import PageNumberPegination
# Create your views here.


class VideoListView(ListView):
    model = Video
    # paginate_by = 10


    def calling(request):
        user_id = request.request.session.get('user')
        meokdauser = meokda_user.objects.get(pk = user_id)
        authoring = meokdauser
        return(request, 'video_list.html', {'authoring' : authoring})



class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'form2.html'


    def form_valid(self, form):
        video = form.save(commit=False)
        user_id = self.request.session.get('user')
        meokdauser = meokda_user.objects.get(pk = user_id)
        video.author = meokdauser
        return super().form_valid(form)
    
    # success_url = '/'


class VideoDetailView(DetailView):
    model = Video


class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'


class VideoDeleteView(DeleteView):
    model = Video