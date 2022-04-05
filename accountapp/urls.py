from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name="accountapp"

urlpatterns = [
    path("hello_world/", hello_world, name='hello_world'),

    # create같은 경우는 특정 View 상속 받아서, 파라미터 설정하고 그랬었는데
    #login,logout은 거창한 것이 필요 없어서 이런식으로 간단하게 해도 된다.
    #login은 템플릿을 지정해 주어야 한다. (로그인 할 때 보는 화면)
    path("login/", LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),

    #class based view에서는 .as_view()를 붙어야 한다.
    path("create/", AccountCreateView.as_view(), name='create'),
    path("update/<int:pk>", AccountUpdateView.as_view(), name='update'),

    #특정유저의 정보를 받으려고 한다. => 고유번호를 받아야 한다
    #detail/<int:pk>  pk라는 이름의 int정보를 받겠다
    path("detail/<int:pk>", AccountDetailView.as_view(), name='detail'),
]
