# from termios import TIOCPKT_DOSTOP
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from .forms import BookListCreateForm
from .models import BookList
import logging
from django.contrib.auth.models import User


class Login(LoginView):
    """ログインページ"""

    model = LoginForm
    template_name = "library/book_login.html"


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""

    template_name = "library/book_login.html"


class IndexView(generic.ListView):
    model = BookList
    template_name = "library/book_list.html"

    def get(self, request, *args, **kwargs):
        # *args:複数の引数をタプルとして受け取る
        # **kwargs:複数のキーワード引数を辞書型オブジェクトとして受け取る
        # FormのGETリクエストのパラメーターは以下のようにして取得できる。
        name = self.request.GET.get("username")
        print(name)
        all_info = request.GET
        print(all_info)

        return super().get(request, **kwargs)

    # def get(self, request, **kwargs):
    #     print("呼ばれた")
    #     print(request.method)
    #     ctx = {
    #         'user': self.request.user
    #     }
    #     print(ctx)
    #     return self.render_to_response(ctx)


class AddView(generic.CreateView):
    model = BookList
    template_name = "library/book_add.html"
    success_url = reverse_lazy("library:main")
    form_class = BookListCreateForm  # TODO 初期値設定
    
    # def get(self, request, *args, **kwargs):
    #     # *args:複数の引数をタプルとして受け取る
    #     # **kwargs:複数のキーワード引数を辞書型オブジェクトとして受け取る
    #     # FormのGETリクエストのパラメーターは以下のようにして取得できる。
    #     name = self.request.GET.get("username")
    #     initial_dict = dict(studentid=name)
    #     form_class = BookListCreateForm(initial=initial_dict)

    #     return super().get(request, **kwargs)


class ReturnView(generic.DeleteView):
    model = BookList
    template_name = "library/book_return.html"
    success_url = reverse_lazy("library:main")
