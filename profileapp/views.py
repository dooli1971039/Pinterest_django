from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:detail') #이 방식으로는 detail페이지로 못 간다.
    #pk를 전해줄 수 없어서. 그래서 내부 메소드를 수정해주어야 한다.
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        #바로 저장하지 않고 임시로 저장 commit=False
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        # self.object가 위에 있는 Profile이다. 따라서 연결되어있는 user의 pk를 얻을 수 있다.

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world') 밑에 get_success_url 있으니 패스
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        # self.object가 위에 있는 Profile이다. 따라서 연결되어있는 user의 pk를 얻을 수 있다.