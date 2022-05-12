from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')  #로그인을 해야 구독을 할 수 있도록 한다.
                                          #post는 굳이 비밀정보가 있는게 아니라서 패스
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):  #projectapp 안에서  detail 페이지 안에서 구독을 할 것임
        # deatil로 향하는데, 향하는 곳이 get방식으로 project_pk를 받아서 그 pk를 가진 detail 페이지로 되돌아감
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) #없는 프로젝트를 구독 신청하면 404
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        if subscription.exists():
            subscription.delete()  #있으면 없애고
        else:
            Subscription(user=user, project=project).save()  #없으면 구독을 만들어준다.
        return super(SubscriptionView, self).get(request, *args, **kwargs)