from django import forms
from .models import Article,BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        
        fields = ['user_name','user_email','body']
        
        widgets = {
            'user_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'input you name',
                'aria-describedby':'sizing-addon1',
            }),
            'user_email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'input you email',
                'aria-describedby':'sizing-addon1',
            }),
            'body':forms.Textarea(attrs={'placeeholder':'say something'}),                
        }
        