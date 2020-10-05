
#######        One Api endpoint 


'''
class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes              =[]
    authentication_classes          =[]
    serializer_class                =StatusSerializer


    def get_queryset(self):
        request       =self.request
        qs            =Status.objects.all()
        query         =request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request         = self.request
        passed_id       = request.GET.get('id')
        queryset        = self.get_queryset()
        # print(type(passed_id))
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
            # print(obj)
        return obj

    def get(self,request,*args,**kwargs):  #this is the overriding the default apilistview
        passed_id     =request.GET.get('id',None)
         
        print(request.body)
        if passed_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    # def patch(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

'''

#####              Tests.py(Status)
'''
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Status
# Create your tests here.

User=get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        user=User.objects.create(username='cfe',email='hello@cfe.com')
        user.set_password('yeahcfe')
        user.save()

    # def test_created_user(self):
    #     qs=User.objects.filter(username='cfe')
    #     self.assertEqual(qs.count(),1)

    def test_creating_status(self):
        user=User.objects.get(username='cfe')
        obj=Status.objects.create(user=user,content='Some cool new content')
        self.assertEqual(obj.id,1)
        qs=User.objects.all()
        self.assertEqual(qs.count(),1)
'''