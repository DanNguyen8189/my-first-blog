from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #which model will be used to create this form
        fields = ('title', 'text',) #which fields should end up in this form