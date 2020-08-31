"""MyApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from CRUD import views or
from CRUD.views import (
    model_detail,
    model_detailview,
    model_listview,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.model_detail) or
    path('',model_detail),
    path('MyApidt/',model_detailview.as_view()),
    path('MyApils/',model_listview.as_view()),
    path('MyApi/Api/',include('CRUD.Api.urls'))
]
