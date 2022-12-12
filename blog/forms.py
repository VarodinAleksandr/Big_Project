from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'discription', 'short_discription', 'is_published', 'picture']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']


class ContactUs(forms.Form):
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=254)
    text = forms.CharField(max_length=512)


