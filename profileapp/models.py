from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    #프로파일의 주인이 누구인지 정해준다
    #OneToOneField Profile과 user객체를 하나씩 연결해준다
    #어디에 연결할지 User객체에 연결,
    #on_deleted : 연결되어있는 User 객체가 사라질 때
    #Cascade : 그와 연결되어있는 profile도 같이 사라진다.
    #related_name : request.user처럼 user 객체에 접근할 때, 따로 profile객체를 찾지 않고 바로 연결해준다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    #upload_to : 이미지를 받아서 서버 내부에 저장하는데 어느 경로에 저장될지 => media/profile~
    #null=True : 이미지 꼭 안 올려도 된다
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)