from django.urls import path

from CRUD.Api.views import (
         Api_detailview,
         Api_listview)


urlpatterns=[
    path('',Api_listview.as_view()),
    path('<int:id>/',Api_detailview.as_view()),
]