from django.db import models

# Create your models here.
class Video(models.Model):
    status_choices = [
      ('before eating', '먹기전'),
      ('eating', '먹는중'),
    ]
    
    restaurant = models.CharField(max_length = 128, verbose_name = '가게이름')
    address = models.CharField(max_length=512, verbose_name='가게주소', null=True)
    foodname = models.CharField(max_length= 128, verbose_name= '음식이름')
    file = models.FileField()
    price = models.PositiveIntegerField(default=0)
    status =  models.CharField(max_length=80, choices= status_choices, null=True)
    mapx = models.FloatField(default=0, verbose_name='X좌표',null=True)
    mapy = models.FloatField(default=0, verbose_name='Y좌표',null=True)
    author = models.CharField(max_length= 150)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = '등록시간')
    updated_at = models.DateTimeField(auto_now = True)