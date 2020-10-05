# import json
# from rest_framework.views import APIView
# # from django.views.generic import View
# from rest_framework import generics,mixins  #use of mixin
# # from rest_framework.generic import List
# # from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# from Status.models import Status
# from .serializers import StatusSerializer

''' This is the previous code of permission


class StatusListSearchAPIView(APIView):
    Permission_classes        =[]
    authentication_classes    =[]

    def get(self,request,format=None):
        qs=Status.objects.all()
        serialize=StatusSerializer(qs,many=True)
        return Response(serialize.data)

    def post(self,request,format=None):
        qs=Status.objects.all()
        serialize=StatusSerializer(qs,many=True)
        return Response(serialize.data)

class StatusAPIView(generics.ListAPIView):
    permission_classes          =[]
    authentication_classes      =[]
    serializer_class            =StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)   
        return qs

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes         =[]
    authentication_classes     =[]
    queryset                   =Status.objects.all()
    serializer_class           =StatusSerializer


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes         =[]
    authentication_classes     =[]
    queryset                   =Status.objects.all()
    serializer_class           =StatusSerializer
    lookup_field               ='id'

    # def get_object(self,*args,**kwargs):
    #     kwargs=self.kwargs
    #     kw_id=kwargs.get('id')
    #     return Status.objects.get(id=kw_id)

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes         =[]
    authentication_classes     =[]
    queryset                   =Status.objects.all()
    serializer_class           =StatusSerializer
    lookup_field               ='id'

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes         =[]
    authentication_classes     =[]
    queryset                   =Status.objects.all()
    serializer_class           =StatusSerializer
    lookup_field               ='id'

'''

'''
          Use of Feature of Mixin
'''
# class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
#     permission_classes          =[]
#     authentication_classes      =[]
#     serializer_class            =StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)   
#         return qs

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class StatusDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
#     permission_classes         =[]
#     authentication_classes     =[]
#     queryset                   =Status.objects.all()
#     serializer_class           =StatusSerializer
#     lookup_field               ='id'

    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)



'''
One Api endpoint 
'''

'''
def is_json(json_data):
    try:
        real_json=json.loads(json_data)
        is_valid=True
    except ValueError:
        is_valid=False
    return is_valid

class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes              =[]
    authentication_classes          =[]
    serializer_class                =StatusSerializer
    passed_id                       =None


    def get_queryset(self):
        request       =self.request
        qs            =Status.objects.all()
        query         =request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request         = self.request
        passed_id       = request.GET.get('id',None) or self.passed_id
        queryset        = self.get_queryset()
        # print(type(passed_id))
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
            # print(obj)
        return obj

    def perform_destroy(self,instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self,request,*args,**kwargs):  #this is the overriding the default apilistview
        url_passed_id     =request.GET.get('id',None)
        json_data         ={}
        body_             =request.body
        
        if is_json(body_):
            json_data     =json.loads(request.body)
        new_passed_id =json_data.get('id',None)
        
        passed_id=url_passed_id or new_passed_id or None
        self.passed_id=passed_id
        # print(passed_id)
        if passed_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        url_passed_id           =request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body

        if is_json(body_):
            json_data=json.loads(body_)
        new_passed_id=json_data.get('id',None)
        requested_id=request.data.get('id',None)
        passed_id=url_passed_id or new_passed_id or requested_id or None
        self.passed_id=passed_id

        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        url_passed_id           =request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body

        if is_json(body_):
            json_data=json.loads(body_)
        new_passed_id=json_data.get('id',None)

        passed_id=url_passed_id or new_passed_id or None
        self.passed_id=passed_id
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        url_passed_id           =request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body

        if is_json(body_):
            json_data=json.loads(body_)
        new_passed_id=json_data.get('id',None)

        passed_id=url_passed_id or new_passed_id or None
        self.passed_id=passed_id
        return self.destroy(request, *args, **kwargs)
'''