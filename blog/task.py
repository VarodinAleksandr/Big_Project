from celery import shared_task
from django.contrib.auth.models import User

# from django.core.mail import send_mail


@shared_task
def send_mail_to_admin(post_id):
    superusers = User.objects.filter(is_superuser=True)
    for user in superusers:
        print(f'new post with id {post_id} was created')
        # send_mail(
        #     'new post created',
        #     f'new post with id {post_id} was created',
        #     'from@example.com',
        #     [user.email],
        #     fail_silently=False,
        # )


@shared_task
def send_mail_to_user(useremal, post_id):
    print(f'new comment with id {post_id} was created')
    # send_mail(
    #     'new comment created',
    #     f'new comment for post with id {post_id} was created',
    #     'from@example.com',
    #     [useremal],
    #     fail_silently=False,
    # )