from rest_framework import serializers
from rest_framework.reverse import reverse

from Status.models import Status
from accounts.api.serializers import UserPublicSerializer
'''
Serializer -> JSON
Serializer -> validate data
'''
# class StatusInlineUserSerializer(serializers.ModelSerializer):
#     uri             = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Status 
#         fields =[
#             'uri',
#             'id',
#             'content',
#             'image'
#         ]

#     def get_uri(self, obj):
#         return "/api/status/{id}/".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    uri  =serializers.SerializerMethodField(read_only=True)
    user =UserPublicSerializer(read_only=True)
    class Meta:
        model=Status
        fields = [
            'user',
            'id',
            'uri',
            'name',
            'content',
            'image'
        ]
        read_only_fields=['user']
    def get_uri(self,obj):
        request=self.context.get('request')
        return reverse('api-status:detail',kwargs={"id":obj.id},request=request)
        # return "status/api/{id}".format(id=obj.id)


    # def validate_content(self,value):
    #     if len(value)>1000:
    #         raise serializers.ValidationError("It is too long")
    #     return value

    def validate(self,data):
        content=data.get("content",None)
        if content=="":
            content=None

        name=data.get("name",None)
        if name=="":
            name=None

        image=data.get("image",None)

        if content is None and name is None and image is None:
            raise serializers.ValidationError("content or image or name is required") 
        return data

# ''' ###Not Working
class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri             = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status 
        fields =[
            'uri',
            'id',
            'content',
            'image'
        ]

    def get_uri(self,obj):
        request=self.context.get('request')
        return reverse('api-status:detail',kwargs={"id":obj.id},request=request)
        # return "/api/status/{id}/".format(id=obj.id)
# '''
    

