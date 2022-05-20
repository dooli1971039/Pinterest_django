from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

from articleapp.models import Article
has_ownership = [account_ownership_required, login_required]



class AccountCreateView(CreateView):  # CreateView를 상속받음
    model = User  # 어떤 모델을 사용할 것이다. #User - 장고에서 기본 제공해주는 모델
    form_class = UserCreationForm  # User 모델을 만들기 위해 사용할 form이 필요하다 #UserCreationForm - 장고가 기본 form을 제공해준다.
    success_url = reverse_lazy('home')  # 계정을 만드는데 성공했다면, 어느 경로로 다시 재연결 할 것인가
    # reverse_lazy(경로)는 reverse()와 기능은 같은데 class에서 사용하는 방식이다.
    template_name = "accountapp/create.html"  # 템플릿을 지정해주어야 한다. (회원가입을 할 때 보는 화면)
    # create.html을 새로 생성하면 당연히 urls.py에도 연결을 해주어야 한다.


# CreateView는 뭔가 만들어야 하니까 form이나 성공했을때 경로 등 정해줘야 하지만, DetailView(reading)은 더 간단하다
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User  # 어떤 모델을 사용할 것인지
    context_object_name = "target_user" #특정 pk유저 정보를 확인하면 그 유저를 보여줘야 한다.
                                        #연예인 인스타 들어갔는데 내 정보가 뜨는게 아니라 그 연예인 정보가 떠야함
    template_name = 'accountapp/detail.html'  # 어떻게 시각화할 것인지

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')
    template_name = "accountapp/update.html"

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'