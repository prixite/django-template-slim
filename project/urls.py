from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(next_page="/"), name="login"),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path("", views.index, name="index"),
]
