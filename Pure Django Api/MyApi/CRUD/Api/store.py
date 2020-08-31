import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import View

from CRUD.models import CRUD as crudmodel
from .mixin import csrfExemptMixin
from CRUD.mixin import HttpResponseMixin
from CRUD.forms import ModelUpdateForm

# write your views here

'''
This is individual CRUD
'''
class Api_detailview(HttpResponseMixin,csrfExemptMixin,View):
    is_json=True

    def get_object(self,id=None):
        '''
        try:
            obj=crudmodel.objects.get(id=id)
        except crudmodel.DoesNotExists:
            obj=None
        '''
        qs=crudmodel.objects.filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None
        
    def get(self,request,id,*args,**kwargs):
        obj=crudmodel.objects.get(id=id)
        json_data=obj.serialize()
        # return HttpResponse(json_data,content_type="application/json")
        self.render_to_response(json_data,status=200)


    def post(self,request,*args,**kwargs):
        json_data=json.dumps({"message":"Not allowed please use /MyApi/Api"})
        return self.render_to_response(json_data,status=403)


    def put(self,request,*args,**kwargs):
        obj=self.get_object(id=id)
        if obj is None:
            error_data=json.dumps({"message":"Update Not Found"})
            return self.render_to_response(error_data,status=404)
        print(request.body)
        new_data=json.loads(request.body)
        print(new_data['content'])
        json_data=json.dumps({"message":"Somethings"})
        return self.render_to_response(json_data)


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
        # print(request.POST)
        # data=json.loads(request.body)
        # print(data)
        form=ModelUpdateForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            data=obj.serialize()
            return self.render_to_response(data,status=201)
        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=403)
        json_data=json.dumps({"message":"Not Allowed"})
        # return HttpResponse(json_data,content_type='application/json',status=400)  "OR"
        return self.render_to_response(json_data,status=403)


    def put(self,request,*args,**kwargs):
        pass


    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({"message":"You cannot delete it"})
        # return HttpResponse(json_data,content_type='application/json',status=403) "OR"
        return self.render_to_response(json_data,status=403)


