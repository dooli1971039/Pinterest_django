from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # POST를 1번 완료한 후에는 GET으로 돌아가게 하자
        # 아래 코드의 뜻은 'accountapp 내부에 있는 hello_world로 재접속하라'라는 의미
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # reverse(경로) 이런 식으로 작성하기 위해서는, 초반에 accountapp/urls.py에 app_name, path안의 name이 지정되어야 한다.
        # reverse()는 (’accountapp:hello_world')에 해당하는 경로를 다시 만들어 주는 역할을 한다.
    else:
        hello_world_list = HelloWorld.objects.all()  # DB에 저장된 list 모두 긁어오기
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):  # CreateView를 상속받음
    model = User  # 어떤 모델을 사용할 것이다. #User - 장고에서 기본 제공해주는 모델
    form_class = UserCreationForm  # User 모델을 만들기 위해 사용할 form이 필요하다 #UserCreationForm - 장고가 기본 form을 제공해준다.
    success_url = reverse_lazy('accountapp:hello_world')  # 계정을 만드는데 성공했다면, 어느 경로로 다시 재연결 할 것인가
    # reverse_lazy(경로)는 reverse()와 기능은 같은데 class에서 사용하는 방식이다.
    template_name = "accountapp/create.html"  # 템플릿을 지정해주어야 한다. (회원가입을 할 때 보는 화면)
    # create.html을 새로 생성하면 당연히 urls.py에도 연결을 해주어야 한다.

# CreateView는 뭔가 만들어야 하니까 form이나 성공했을때 경로 등 정해줘야 하지만, DetailView(reading)은 더 간단하다
class AccountDetailView(DetailView):
    model = User  # 어떤 모델을 사용할 것인지
    context_object_name = "target_user" #특정 pk유저 정보를 확인하면 그 유저를 보여줘야 한다.
                                        #연예인 인스타 들어갔는데 내 정보가 뜨는게 아니라 그 연예인 정보가 떠야함
    template_name = 'accountapp/detail.html'  # 어떻게 시각화할 것인지
