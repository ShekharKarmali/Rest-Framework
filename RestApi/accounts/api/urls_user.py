from django.contrib import admin
from django.urls import path,include

from accounts.api.user.views import UserDetailAPIView
urlpatterns = [
    path('<str:username>/',UserDetailAPIView.as_view(),name='detail'),
]
