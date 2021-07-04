from django.urls import path
from . import views
from .models import Video

from django.conf.urls import url


app_name = 'video'

urlpatterns = [ 
    path('',views.VideoListView.as_view(), name='video_list'),
    path('new/', views.VideoCreateView.as_view(), name = 'video_new'),
    path('<int:pk>/edit/',views.VideoDetailView.as_view(), name = 'video_edit'),
    path('<int:pk>/delete/',views.VideoDeleteView.as_view(), name = 'video_delete'),
    path('UserProfile/<str:username2>/', views.UserProfile),
    path('new_sup/', views.Search_try, name='search'),
]