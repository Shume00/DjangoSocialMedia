# Generated by Django 4.0.5 on 2022-06-17 19:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Domashno', '0005_alter_blogpost_lastchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='blockedUser',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='blocked_users', to=settings.AUTH_USER_MODEL),
        ),
    ]