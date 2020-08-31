import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.generic import View

from CRUD.models import CRUD as crudmodel
from .mixin import csrfExemptMixin
from CRUD.mixin import HttpResponseMixin
from CRUD.forms import ModelUpdateForm
from .utils import is_json

# write your views here
'''
This is individual CRUD
'''

# class Api_detailview(HttpResponseMixin,csrfExemptMixin,View):
#     is_json=True

#     def get_object(self,id=None):
#         '''
#         try:
#             obj=crudmodel.objects.get(id=id)
#         except crudmodel.DoesNotExists:
#             obj=None
#         '''
#         qs=crudmodel.objects.filter(id=id)
#         if qs.count()==1:
#             return qs.first()
#         return None

#     def get(self,request,id,*args,**kwargs):
#         obj=crudmodel.objects.get(id=id)
#         json_data=obj.serialize()
#         # return HttpResponse(json_data,content_type="application/json")
#         self.render_to_response(json_data,status=200)


#     def post(self,request,*args,**kwargs):
#         json_data=json.dumps({"message":"Not allowed please use /MyApi/Api"})
#         return self.render_to_response(json_data,status=403)


#     def put(self,request,id,*args,**kwargs):
#         '''
#         #json validation
#         valid_json=is_json(request.body)
#         if not valid_json:
#             error_data=json.dumps({"message":"Invalid data sent please sent using json"})
#             return self.render_to_response(error_data,status=400)
        
#         #object validation
#         obj=self.get_object(id=id)
#         if obj is None:
#             error_data=json.dumps({"message":"Update Not Found"})
#             return self.render_to_response(error_data,status=404)
        
#         #fetching changing data
#         data=json.loads(obj.serialize())
#         passed_data=json.loads(request.body)
#         for key,value in passed_data.items():
#             data[key]=value
        
#         #saving all the content
#         form=ModelUpdateForm(data,instance=obj)
#         if form.is_valid():
#             obj=form.save(commit=True)
#             obj_data=json.dumps(data)
#             return self.render_to_response(obj_data,status=201)
#         if form.errors:
#             data=json.dumps(form.errors)
#             return self.render_to_response(data,status=400)

#         json_data=json.dumps({"message":"Something"})
#         return self.render_to_response(json_data)

      
#     def delete(self,request,id,*args,**kwargs):
#         obj=self.get_object(id=id)
#         if obj is None:
#             error_data=json.dumps({"message":"update not found"})
#             return self.render_to_response(error_data,status=404)
#         deleted_=obj.delete()
#         print(deleted_)
#         json_data=json.dumps({"message":"deleted successfully"})
#         return self.render_to_response(json_data,status=200)
#         '''

# '''
# This is Group/List  CRUD
# '''

# class Api_listview(HttpResponseMixin,csrfExemptMixin,View):
#     is_json=True

#     def get(self,request,*args,**kwargs):
#         qs=crudmodel.objects.all()
#         json_data=qs.serialize()
#         # return HttpResponse(json_data,content_type="application/json",status=200) "OR"
#         return self.render_to_response(json_data,status=200)
            


#     def post(self,request,*args,**kwargs):
#         # print(request.POST)
#         # data=json.loads(request.body)
#         # print(data)
#         form=ModelUpdateForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=True)
#             data=obj.serialize()
#             return self.render_to_response(data,status=201)
#         if form.errors:
#             data=json.dumps(form.errors)
#             return self.render_to_response(data,status=403)
#         json_data=json.dumps({"message":"Not Allowed"})
#         # return HttpResponse(json_data,content_type='application/json',status=400)  "OR"
#         return self.render_to_response(json_data,status=403)


#     def put(self,request,*args,**kwargs):
#         pass


#     def delete(self,request,*args,**kwargs):
#         json_data=json.dumps({"message":"You cannot delete it"})
#         # return HttpResponse(json_data,content_type='application/json',status=403) "OR"
#         return self.render_to_response(json_data,status=403)


### This is the part of one endpoint to rule the world
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


    def put(self,request,id,*args,**kwargs):
       pass

    def delete(self,request,id,*args,**kwargs):
        obj=self.get_object(id=id)
        if obj is None:
            error_data=json.dumps({"message":"update not found"})
            return self.render_to_response(error_data,status=404)
        deleted_=obj.delete()
        print(deleted_)
        json_data=json.dumps({"message":"deleted successfully"})
        return self.render_to_response(json_data,status=200)


'''
This is Group/List  CRUD
'''

class Api_listview(HttpResponseMixin,csrfExemptMixin,View):
    is_json=True
    queryset=None

    def get_queryset(self):
            qs=crudmodel.objects.all()
            self.queryset=qs
            return qs

    def get_object(self,id=None):
        '''
        try:
            obj=crudmodel.objects.get(id=id)
        except crudmodel.DoesNotExists:
            obj=None
        '''
        # qs=crudmodel.objects.filter(id=id)
        # if qs.count()==1:
        #     return qs.first()
        # return None

        if id is None:
           return None
        qs=self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

    def get(self,request,*args,**kwargs):
        data=json.loads(request.body)
        passed_id=data.get("id",None)
        if passed_id is not None:
            obj=self.get_object(id=passed_id)
            if obj is  None:
                error_data=json.dumps({"message":"Object not found"})
                return self.render_to_response(error_data,status=400)
            json_data=obj.serialize()
            return self.render_to_response(json_data,status=200)
        else:
            qs=self.get_queryset()
            json_data=qs.serialize()
            return self.render_to_response(json_data)

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


    def put(self,request,*args,**kwargs):  #put function is written and is running successfully.
        is_valid=is_json(request.body)
        if not is_valid:
            error_data=json.dumps({"message":"Invalid data sent,sent in json format"})
            return self.render_to_response(error_data,status=400)
        
        passed_data=json.loads(request.body)
        passed_id=passed_data.get('id',None)
        if not passed_id:
            error_code=json.dumps({"message":"This field requires id"})
            return self.render_to_response(error_code,status=400)

        obj=self.get_object(id=passed_id)
        if obj is None:
            error_code=json.dumps({"message":"Object is not found"})
            return self.render_to_response(error_code,status=404)

        data=json.loads(obj.serialize())
        for key,value in passed_data.items():
            data[key]=value

        form=ModelUpdateForm(data,instance=obj)
        if form.is_valid():
            obj=form.save(commit=True)
            obj_data=json.dumps(data)
            return self.render_to_response(obj_data,status=200)
        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=401)

        json_data=json.dumps({"message":"Somethings is here"})
        return self.render_to_response(error_data,status=404)

    def delete(self,request,*args,**kwargs): #This funtion too running successfully 
        # Json validation
        is_valid=is_json(request.body)
        if not is_valid:
            error_data=json.dumps({"message":"Invalid data sent,sent in json format"})
            return self.render_to_response(error_data,status=400)
        
        # Id validation
        passed_data=json.loads(request.body)
        passed_id=passed_data.get('id',None)
        if not passed_id:
            error_code=json.dumps({"message":"This field requires id"})
            return self.render_to_response(error_code,status=400)

        # Object validation
        obj=self.get_object(id=passed_id)
        if obj is None:
            error_code=json.dumps({"message":"Object is not found"})
            return self.render_to_response(error_code,status=404)

        deleted_=obj.delete()
        print(deleted_)
        json_data=json.dumps({"message":"deleted successfully"})
        return self.render_to_response(json_data,status=200)