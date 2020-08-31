
'''
                        This all is extra part of django pure rest api and some basic fundamental
'''

# ###                                    ______Modals______
def serialize(self):
        qs=self
        return serialize("json",qs,fields=('user','content','image'))

        OR

def serialize(self):
    qs=self
    final_array=[]
    for obj in qs:
        stuc=json.loads(obj.serialize())
        final_array.append(stuc)
        # final_array.append(obj.serialize())
    return json.dumps(final_array)
    # return final_array


# ###                                     ______Class Based View_____

class JsonCBV1(View):
    def get(self,request,*args, **kwargs):

        data={
         "count":1000,
         "content": "Some new content have been added"
        }

        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs): 
        data={
            "count":200,
            "content": "Some new content have been added"
        }

        return self.render_to_json_response(data)

'''
class SerialisedDetail(View):
    def get(self,request,*args,**kwargs):
        obj=Update.objects.get(id=1) 
        data={
            "user": obj.user.username,
            "content": obj.content
        }
        json_data=json.dumps(data)
        return HttpResponse(json_data,content_type='application/json')
'''


# This is one id output as list
class SerialisedDetail(View):
    def get(self,request,*args,**kwargs):
        obj=Update.objects.get(id=1) 
        data=serialize("json",[obj,],fields=('user','content'))
        json_data=data
        return HttpResponse(json_data,content_type='application/json')

class SerialisedList(View):
    def get(self,request,*args,**kwargs):
        qs=Update.objects.all() 
        data=serialize("json",qs,fields=('user','content'))
        json_data=data
        return HttpResponse(json_data,content_type='application/json')


# ###                  ____Modular Function_____

class JsonResponseMixin(object):
    def render_to_json_response(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context),**response_kwargs)

    def get_data(self,context):
        return context