from django import forms
from questions.models import Question,Answer
from taggit.forms import * 

class CreateNewQuestionForm(forms.ModelForm):
    question = forms.CharField(
        max_length=255,
        required=True,
        label= '',
        widget= forms.widgets.TextInput(
            attrs= {
                "placeholder": "Ask Question",
                "class":'custom-input'
            }))
    tags = TagField(
        required=True,
        label='',
        help_text= 'add Comma after each tag',
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder':'Add some tags here',
                'class':'custom-tag-input',
               
            }))
    class Meta:
        model= Question
        fields= ['question','tags']
            
    