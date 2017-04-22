# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 10:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogs', '0004_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='votes',
        ),
        migrations.AddField(
            model_name='blog',
            name='downvotes',
            field=models.ManyToManyField(related_name='blog_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='upvotes',
            field=models.ManyToManyField(related_name='blog_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
