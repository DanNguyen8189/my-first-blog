from django import forms

from .models import Post, Comment

# this class allows users to edit posts
class PostForm(forms.ModelForm):

    class Meta:
        model = Post #which model will be used to create this form
        fields = ('title', 'text',) #which fields should end up in this form

# lets users add comments
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)