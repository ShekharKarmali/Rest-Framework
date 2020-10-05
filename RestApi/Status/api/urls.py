from django.urls import path
# from django.conf.urls import url

from .views import (
    # StatusListSearchAPIView, 
    StatusAPIView,
    StatusDetailAPIView,
    # StatusCreateAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

app_name = 'Status'
# write your urls
urlpatterns=[
    # path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view(),name='list'),
    path('<int:id>/', StatusDetailAPIView.as_view(),name='detail'),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]