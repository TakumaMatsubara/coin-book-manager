# from termios import TIOCPKT_DOSTOP
from datetime import timezone
import django
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

# LoginViewはログオン機能
# LogoutViewはログアウト機能
# LoginRequiredMixinはログインしたユーザーだけ閲覧できるように制限する

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = "library/book_login.html"

# 複数のクラスを承継する場合は、LoginRequiredMixinを一番最初に指定.これをしないとエラーが出るかも．

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""

    template_name = "library/book_login.html"


class IndexView(generic.ListView):
    model = BookList
    template_name = "library/book_list.html"

    def get(self, request, *args, **kwargs):
        # *args:複数の引数をタプルとして受け取る
        # **kwargs:複数のキーワード引数を辞書型オブジェクトとして受け取る
        user = self.request.user
        print(user)

        return super().get(request, **kwargs)

    # def get(self, request, **kwargs):
    #     print("呼ばれた")
    #     print(request.method)
    #     ctx = {
    #         'user': self.request.user
    #     }
    #     print(ctx)
    #     return self.render_to_response(ctx)
        # FormのGETリクエストのパラメーターは以下のようにして取得できる。
        # all_info = request.GET
        # print(all_info)

# def add(request):
#     model = BookList
#     form = BookListCreateForm(initial={
#             'studentid': model.studentid,
#         })
#     context = { 'form': form }
#     return render(request, 'library/book_add.html', context)

class AddView(generic.CreateView):
    success_url = reverse_lazy("library:main")
    model = BookList
    template_name = "library/book_add.html"
    success_url = reverse_lazy("library:main")
    form_class = BookListCreateForm
    # def get(self, request, **kwargs):
    #     initial_dict = {"studentid": self.request.user}
    #     form = BookListCreateForm(request.GET or None, initial=initial_dict)
    #     return render(request, "library/book_add.html", dict(dorm=form))
    #     # return super().get(request, **kwargs)

    # def get(self, request, *args, **kwargs):
            # model = BookList
        # template_name = "library/book_add.html"
        # print(self.request.use)
        # form_class = BookListCreateForm(initial=initial_dict)
        # ctx = {"form": form_class}
        # return render(request, template_name, ctx)

        # form_class = BookListCreateForm  # TODO 初期値設定
    # def get(self, request):
    #     initial_dict = dict(studentid="takuma")

    #     return render(request, "library/book_add.html", dict(form=form))
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
