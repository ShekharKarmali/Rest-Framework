from django.contrib.auth import get_user_model
from rest_framework import generics, permissions,pagination
from rest_framework.response import Response
from accounts.api.permissions import AnonPermissionOnly


from Status.api.serializers import StatusInlineUserSerializer
from Status.models import Status
from Status.api.views import StatusAPIView

from .serializers import UserDetailSerializer


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    #permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    queryset            = User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username' # id

    def get_serializer_context(self):
        return {'request': self.request}

class UserStatusAPIView(StatusAPIView):
    serializer_class            = StatusInlineUserSerializer
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)

# class CustomPagination(pagination.PageNumberPagination):
#     page_size = 2

# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class    = StatusInlineUserSerializer
#     # pagination_class    = pagination.PageNumberPagination
#     pagination_class    = CustomPagination
#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get("username", None)
#         # print(username)
#         if username is None:
#             return Status.objects.none()
#         return Status.objects.filter(user__username=username)
