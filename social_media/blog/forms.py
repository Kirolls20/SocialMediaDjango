from django import forms

from blog.models import Blog,Author

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

