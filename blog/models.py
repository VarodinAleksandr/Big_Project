from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .task import send_mail_to_admin, send_mail_to_user
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300)
    discription = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    short_discription = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='upload/')

    def __str__(self):
        return f'post with id {self.id}, title: {self.title}, short discription: {self.short_discription}'


@receiver(post_save, sender=Post)
def new_post_notification(instance, created, **kwargs):
    if created:
        send_mail_to_admin.apply_async(args=(instance.id,))


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    is_published = models.BooleanField(default=False)
    username = models.CharField(max_length=255)

    def __str__(self):
        return f'comment from {self.username} for post id {self.post.id}'

    def post_url(self):
        return reverse('blog:post_detail', args=[self.post.id])


@receiver(post_save, sender=Comment)
def new_comment_notification(instance, created, **kwargs):
    if created:
        user_email = instance.post.owner.email
        send_mail_to_user.apply_async(args=(user_email, instance.post_url()))
