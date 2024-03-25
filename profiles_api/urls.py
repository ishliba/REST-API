from django.contrib import admin
from django.urls import path, include
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloAPiView.as_view()),

]
