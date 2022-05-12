from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription') #지워지면 같이 지워짐
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription') #지워지면 같이 지워짐

    class Meta:
        unique_together = ('user', 'project')  #같은 게시판을 여러번 구독할 수는 없게 해야함