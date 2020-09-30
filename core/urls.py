from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "core"

urlpatterns = [
    path('',views.HomeView.as_view(), name='homeview'),
    path('login',LoginView.as_view(),name='login'),
    path('register', views.register, name='register'),
]
