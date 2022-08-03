from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='users.index'),
    path("users", views.users, name='users.home')
]
