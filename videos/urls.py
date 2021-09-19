from django.urls import path
from . import views

app_name = "videos"
urlpatterns = [
    path('', views.main, name="main"),
    path('upload/', views.upload, name="upload"),
]
