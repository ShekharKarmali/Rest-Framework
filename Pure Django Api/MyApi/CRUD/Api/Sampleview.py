import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import View

from CRUD.models import CRUD as crudmodel
from .mixin import csrfExemptMixin
from CRUD.mixin import HttpResponseMixin

# write your views here

'''
This is individual CRUD
'''
class Api_detailview(HttpResponseMixin,csrfExemptMixin,View):
    def get(self,request,id,*args,**kwargs):
        obj=crudmodel.objects.get(id=id)
        json_data=obj.serialize()
        return HttpResponse(json_data,content_type="application/json")


    def post(self,request,*args,**kwargs):
        pass


    def update(self,request,*args,**kwargs):
        pass


    def delete(self,request,*args,**kwargs):
        pass


'''
This is Group/List  CRUD
'''

class Api_listview(HttpResponseMixin,csrfExemptMixin,View):
    is_json=True

    def get(self,request,*args,**kwargs):
        qs=crudmodel.objects.all()
        json_data=qs.serialize()
        # return HttpResponse(json_data,content_type="application/json",status=200) "OR"
        return self.render_to_response(json_data,status=200)
            


    def post(self,request,*args,**kwargs):
        json_data=json.dumps({"message":"You can post it"})
        # return HttpResponse(json_data,content_type='application/json',status=400)  "OR"
        return self.render_to_response(json_data,status=400)


    def update(self,request,*args,**kwargs):
        pass


    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({"message":"You cannot delete it"})
        # return HttpResponse(json_data,content_type='application/json',status=403) "OR"
        return self.render_to_response(json_data,status=403)


