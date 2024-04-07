from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewset)


urlpatterns = [
    path('hello-view/', views.HelloAPiView.as_view()),
    path('login/', views.UserloginApiView.as_view()),  #for login
    path('', include(router.urls))

    ]