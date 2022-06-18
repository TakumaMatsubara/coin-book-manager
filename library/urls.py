from django.urls import path, include
from . import views

app_name = "library"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("main/", views.IndexView.as_view(), name="main"),
    path("add/", views.AddView.as_view(), name="add"),
    path("return/<int:pk>/", views.ReturnView.as_view(), name="return"),
]