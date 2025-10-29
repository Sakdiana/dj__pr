from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['author','title','content']
        widgets={
            'author':forms.TextInput(attrs={'class':'input','placeolder':"Автор"}),
            'title':forms.TextInput(attrs={'class':'input','placeolder':"Заголовок"}),
            'content':forms.TextInput(attrs={'class':'input','placeolder':"Контент"}),
            
        }