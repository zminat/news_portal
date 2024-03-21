# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
#
# from .models import PostCategory
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def post_created(instance, sender, **kwargs):
#     if kwargs['action'] != 'post_add':
#         return
#
#     is_first = True
#     emails = []
#     subject = 'Новая новость в категориях: '
#     for category in instance.postCategory.all():
#         emails += User.objects.filter(
#             subscriptions__category=category
#         ).values_list('email', flat=True)
#         if is_first:
#             subject += f'{category}'
#             is_first = False
#         else:
#             subject += f', {category}'
#
#     text_content = (
#         f'{instance.title}\n'
#         f'{instance.preview()}\n\n'
#         f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'{instance.title}<br>'
#         f'{instance.preview()}<br><br>'
#         f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#         f'Ссылка на новость:</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()