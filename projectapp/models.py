from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False) #이미지
    title = models.CharField(max_length=20, null=False) #타이틀
    description = models.CharField(max_length=200, null=True) #프로젝트 설명

    created_at = models.DateTimeField(auto_now=True) #언제 만들어졌는지