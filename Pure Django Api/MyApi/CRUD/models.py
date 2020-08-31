import json
from django.db import models
from django.conf import settings
from django.core.serializers import serialize

# Create your models here.

def upload_updated_image(instance,filename):
    return '/MyApi/{user}/{filename}'.format(user=instance.user,filename=filename)

class UpdateQueryset(models.QuerySet):
    def serialize(self):
        # dot value method
        list_value=list(self.values("user","id","name","content","image"))                                           
        return json.dumps(list_value)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(self.model,using=self.db)

class CRUD(models.Model):
    user               =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name               =models.TextField(blank=True,null=True)
    content            =models.TextField(blank=True,null=True)
    image              =models.ImageField(upload_to=upload_updated_image,null=True,blank=True)
    updated            =models.DateTimeField(auto_now=True)
    timestamp          =models.DateTimeField(auto_now_add=True)
    
    # This is modellistview
    objects=UpdateManager()

    def __str__(self):
        return self.name or ""

    
    #This is for modeldetailview
    def serialize(self):
        try:
            image=self.image.url
        except:
            image=""
        data={
            "user":self.user.id,
            "id":self.id,
            "name":self.name,
            "content":self.content,
            "image":image
        }

        return json.dumps(data)
