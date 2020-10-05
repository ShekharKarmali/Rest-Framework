from django.contrib import admin
from .models import Status
from .forms import StatusForm
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display=['user','name','__str__','image']
    form=StatusForm  #This is used instead of meta class to have look list display in admin 
    # class Meta:
    #     model=Status

admin.site.register(Status,StatusAdmin)
