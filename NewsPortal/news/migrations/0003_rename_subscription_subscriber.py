# Generated by Django 4.2.10 on 2024-03-14 11:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_subscription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='Subscriber',
        ),
    ]