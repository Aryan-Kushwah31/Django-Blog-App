from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("signup/", views.signup, name='signup'),
    path("create/", views.create, name='create'),
    path("content/<int:pk>", views.content, name='content'),
    path("delete/<int:pk>", views.delete_view, name='delete'),
]