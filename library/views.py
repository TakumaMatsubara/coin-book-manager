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


class AddView(generic.CreateView):
    success_url = reverse_lazy("library:main")
    model = BookList
    #template_name = "library/book_add.html"
    success_url = reverse_lazy("library:main")
    form_class = BookListCreateForm
    def get(self, request, **kwargs):
        initial_dict = {"studentid": self.request.user}
        form = BookListCreateForm(request.GET or None, initial=initial_dict)
        return render(request, "library/book_add.html", dict(form=form))

class ReturnView(generic.DeleteView):
    model = BookList
    template_name = "library/book_return.html"
    success_url = reverse_lazy("library:main")
