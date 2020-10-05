import json
from rest_framework import generics, mixins,permissions
from rest_framework.authentication  import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import filters
# import django_filters.rest_framework

from Status.models import Status
from .serializers import StatusSerializer
from accounts.api.permissions import IsOwnerOrReadOnly

# # CreateModelMixin --- POST method
# # UpdateModelMixin --- PUT method
# # DestroyModelMixin -- DELETE method
def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class StatusDetailAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin, 
    generics.RetrieveAPIView):
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    # authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None



class StatusAPIView(
    mixins.CreateModelMixin, 
    generics.ListAPIView): 
    permission_classes          = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes      = [SessionAuthentication]
    serializer_class            = StatusSerializer
    passed_id                   = None
    filter_backends             = [filters.SearchFilter,filters.OrderingFilter]
    # filter_backends             = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields               = ['user__username','content']
    # ordering_fields             = '__all__'
    ordering_fields             = ['user__username','timestamps']
    queryset                    =Status.objects.all()

    # def get_queryset(self):
    #     request = self.request
    #     print(request.user)
    #     qs = Status.objects.all()
    #     query = request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

