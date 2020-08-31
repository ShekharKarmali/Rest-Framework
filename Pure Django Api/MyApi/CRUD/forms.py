from django import forms

from .models import CRUD as crudmodel

class ModelUpdateForm(forms.ModelForm):
    class Meta:
        model=crudmodel
        fields=[
            'user',
            'name',
            'content',
            'image'
        ]

    def clean(self,*args,**kwargs):
        data=self.cleaned_data
        content=data.get('content' or None)
        if content=="":
            content=None
        name=data.get('name' or None)

        if content is None or name is None:
            raise forms.ValidationError("content or name is not given")
        return super().clean(*args,**kwargs)
        # return data //we can also write this
