from django import forms


from .models import Status

#write your form data

class StatusForm(forms.ModelForm):
    class Meta:
        model=Status
        fields=[
            'user',
            'content',
            'name',
            'image'
        ]

    def clean_content(self,*args,**kwargs):
        content=self.cleaned_data.get('content',None)
        if len(content)>250:
            raise forms.ValidationError("Content is too long")
        return content


    def clean(self,*args,**kwargs):
        data=self.cleaned_data
        content=data.get('content',None)
        if content=="":
            content=None
        name=data.get('name',None)
        if name=="":
            name=None
        image=data.get("image",None)
        if content is None and name is None and image is None:
            raise forms.ValidationError("Content or name or image is required")
        return super().clean(*args,**kwargs)


