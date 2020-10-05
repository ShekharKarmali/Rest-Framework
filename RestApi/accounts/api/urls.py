from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import AuthView,RegisteView

app_name='accounts'

urlpatterns = [
    path('',AuthView.as_view(),name='login'),
    path('register/',RegisteView.as_view(),name='register'),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]
