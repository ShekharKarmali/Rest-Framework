import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.views.generic import View

from .models import CRUD as crudmodel
# Create your views here.
'''
This is function based view
'''

def model_detail(request):
    data={
        "hash_no.":121,
        "status":"check"
    }
    # return JsonResponse(data)
    # little modification
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')

'''
This is class based view in serialised
'''

'''
class model_detailview(View):
    def get(self,request,*args,**kwargs):
        obj=crudmodel.objects.get(id=1) 
        data=serialize("json",[obj,],fields=('user','name','content'))
        json_data=data
        return HttpResponse(json_data,content_type='application/json')


class model_listview(View):
    def get(self,request,*args,**kwargs):
        qs=crudmodel.objects.all() 
        data=serialize("json",qs,fields=('user','name','content'))
        json_data=data
        return HttpResponse(json_data,content_type='application/json')
'''
# "OR" this one but its serialise function must be on models.py

class model_detailview(View):
    def get(self,request,*args,**kwargs):
        obj=crudmodel.objects.get(id=1)
        json_data=obj.serialize()
        return HttpResponse(json_data,content_type='application/json')


class model_listview(View):
    def get(self,request,*args,**kwargs):
        qs=crudmodel.objects.all()
        json_data=qs.serialize()
        return HttpResponse(json_data,content_type='application/json')



    
