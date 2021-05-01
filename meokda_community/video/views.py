from django.db.models.query_utils import select_related_descend
from django.shortcuts import render,redirect
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


# import simplejson as json
# from rest_framework import generics
# from rest_framework.pagination import PageNumberPegination
# Create your views here.


class VideoListView(ListView):
    model = Video
    paginate_by = 4
    context_object_name = 'video_list'
    template_name = 'video/video_list.html'

def index(request):
    return render(request, 'index.html', {'username' : request.session.get('user')})


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
    
    # success_url = '/'


class VideoDetailView(DetailView):
    model = Video


class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'


class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('video:video_list')


from django.views.generic.list import ListView
from .models import Article

class ArticlesView(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'videos'
    template_name = 'video/articles.html'



