from celery import shared_task
from django.contrib.auth.models import User

from django.core.mail import send_mail


@shared_task
def send_mail_to_admin(post_id):
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        print(f'new post with id {post_id} was created')
        send_mail(
            'new post created',
            f'new post with id {post_id} was created',
            'from@example.com',
            [user.email],
            fail_silently=True,
        )


@shared_task
def send_mail_to_user(useremal, post_url):
    print(f'new comment with id {post_url} was created')
    superusers = User.objects.filter(is_superuser=True)
    emails = [i.email for i in superusers]
    emails.append(useremal)
    for e in emails:
        send_mail(
            'new comment created',
            f'new comment for post with id {post_url} was created',
            'from@example.com',
            [e],
            fail_silently=True,
        )


@shared_task
def send_contact_us_email(email, text):
    print('Send contact us email')
    send_mail(
        'You have new message from contact us',
        text,
        'from@example.com',
        [email],
        fail_silently=True,
    )
