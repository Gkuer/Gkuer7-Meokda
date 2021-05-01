from django.db import models
from django.conf import settings
from django.urls import reverse
from django.views.generic.detail import DetailView

# Create your models here.


class Video(models.Model):
    status_choices = {
      ('before eating', '먹기전'),  # 오른쪽에 있는 것이 화면에 보인다.
      ('eating', '먹는중'),
  }

    restaurant = models.CharField(max_length = 128, verbose_name = '가게이름')
    foodname = models.CharField(max_length= 128, verbose_name= '음식이름')
    file = models.FileField()

    price = models.PositiveIntegerField(default=0)
    status =  models.CharField(max_length=80, choices= status_choices, null=True)
    distance = models.PositiveIntegerField(default=0, verbose_name='거리')


    title = models.CharField(max_length= 128, verbose_name= '제목', default= '모르겠어요')
    author = models.ForeignKey('user.meokda_user', on_delete = models.CASCADE, verbose_name = '작성자', null = True )
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = '등록시간')
    updated_at = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse('video:video_list')
    
    class Meta:
      ordering = ['-created_at']



class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField()
    author = models.CharField(max_length=30)
    file = models.FileField(null=True)


