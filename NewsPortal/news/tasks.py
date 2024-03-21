import datetime
from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import PostCategory, Post
from datetime import timezone


@shared_task
def send_new_post(pk):
    instance = Post.objects.get(pk=pk)
    is_first = True
    emails = []
    subject = 'Новая публикация в категориях: '
    for category in instance.postCategory.all():
        emails += User.objects.filter(
            subscriptions__category=category
        ).values_list('email', flat=True)
        if is_first:
            subject += f'{category}'
            is_first = False
        else:
            subject += f', {category}'

    text_content = (
        f'{instance.title}\n'
        f'{instance.preview()}\n\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'{instance.title}<br>'
        f'{instance.preview()}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на публикацию:</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task
def weekly_news():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(User.objects.filter(subscriptions__category__name__in=categories).values_list('email', flat=True))

    for subscriber in subscribers:
        html_content = render_to_string(
            'daily_post.html',
            {
                'link': settings.SITE_URL,
                'posts': posts,
            }
        )
        msg = EmailMultiAlternatives(
            subject='Статьи за неделю',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[subscriber],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
