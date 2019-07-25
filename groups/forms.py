from django import forms
from django.template.defaultfilters import slugify



class add_group(forms.Form):
    name = forms.CharField(label = 'Group Name', widget = forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(label = 'Group Description',widget = forms.Textarea(attrs={'class':'form-control'}))




    

    


