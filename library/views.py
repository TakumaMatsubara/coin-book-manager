from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm

from .forms import BookListCreateForm
from .models import BookList

class Login(LoginView):
    """ログインページ"""
    moddel = LoginForm
    template_name = 'library/book_login.html'

class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'library/book_login.html'

class IndexView(generic.ListView):
    model = BookList
    template_name = 'library/book_list.html'

class AddView(generic.CreateView):
    model = BookList
    template_name = 'library/book_add.html'
    success_url = reverse_lazy('library:main')
    form_class = BookListCreateForm

class ReturnView(generic.DeleteView):
    model = BookList
    template_name = 'library/book_return.html'
    success_url = reverse_lazy('library:main')
