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


# import simplejson as json
# from rest_framework import generics
# from rest_framework.pagination import PageNumberPegination
# Create your views here.

# 메인화면
class VideoListView(ListView):
    model = Video
    paginate_by = 4
    context_object_name = 'video_list'
    template_name = 'video/video_list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(VideoListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['ddd'] = meokda_user.objects.filter(username=self.request.session.get('user'))
        return context


# 비디오 업로드
@method_decorator(login_required, name='dispatch')
class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'form2.html'
    def form_valid(self, form):
        video = form.save(commit=False)
        user_id = self.request.session.get('user')
        meokdauser = meokda_user.objects.get(username = user_id)
        video.author = meokdauser
        return super().form_valid(form)
    


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
    