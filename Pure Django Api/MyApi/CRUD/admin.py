from django.contrib import admin

from .models import CRUD as crudmodel

# Register your models here.
admin.site.register(crudmodel)
