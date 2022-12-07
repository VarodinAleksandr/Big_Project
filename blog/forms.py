from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'discription', 'short_discription', 'is_published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

