from django import forms
from django.template.defaultfilters import slugify



class add_post(forms.Form):
    title = forms.CharField(label = 'Title' ,widget = forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(label = 'Body',widget = forms.Textarea(attrs={'class':'form-control'}))
   

    

    