from django.urls import path
from . import views

urlpatterns = [
    path('users/login', views.login_view, name='login_view'),
]