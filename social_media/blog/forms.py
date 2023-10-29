from django import forms
from taggit.forms import *
from blog.models import Blog
# from users.models import User


class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        required=True,
        label='',
        widget = forms.widgets.TextInput(
            attrs={
                'placeholder':'Blog Title',
                'class':'custom-input' ,
            }))
    tags = TagField(
        required=True,
        label='',
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Add some tags here',
                'class':'custom-tag-input',
            }))
            
    body= forms.CharField(
        required=True,
        label='',
        widget = forms.widgets.Textarea(
            attrs={
                'placeholder':'Blog Body',
                'class':'custom-textarea',
            }))
  
    class Meta:
        model=Blog
        fields= ['title','tags','body']


class SearchForm(forms.Form):
    input = forms.CharField(max_length=128,label='',widget=forms.widgets.TextInput(
        attrs={
            'placeholder':'Search By Tags',
        }
    ))