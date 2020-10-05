from django.db import models
from django.conf import settings

# Create your models here.

def upload_status_image(instance,filename):
    return "Status/{user}/{filename}".format(user=instance.user,filename=filename)
class StatusQueryset(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_Queryset(self):
        return StatusQueryset(self.model,using=self._db)

class Status(models.Model):
    user           =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name           =models.TextField(null=True,blank=True)
    content        =models.TextField(null=True,blank=True)
    image          =models.ImageField(upload_to=upload_status_image,null=True,blank=True)
    updated        =models.DateTimeField(auto_now=True)
    timestamps     =models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50] #this is lenght of content to be display on django admin Page
        # return str(self.name)

    class Meta:
        verbose_name='Status post'
        verbose_name_plural='Status posts'

    @property
    def owner(self):
        return self.user