from django.urls import path
from . import views
from .models import Video

from django.conf.urls import url
from .views import UserProfile

app_name = 'video'

urlpatterns = [ 
    path('',views.VideoListView.as_view(), name='video_list'),
    path('new/', views.VideoCreateView.as_view(), name = 'video_new'),
    path('<int:pk>/edit/',views.VideoDetailView.as_view(), name = 'video_edit'),
    path('<int:pk>/delete/',views.VideoDeleteView.as_view(), name = 'video_delete'),
    path('test/',views.ArticlesView.as_view(), name='articles'),
    path('<int:pk>/', UserProfile.as_view()),
]