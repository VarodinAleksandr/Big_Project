from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    discription = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    short_discription = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='')

    def __str__(self):
        return f'post with id {self.id}, title: {self.title}, short discription: {self.short_discription}'


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text
