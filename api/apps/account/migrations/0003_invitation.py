# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 14:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160429_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('sent', models.DateTimeField(null=True)),
                ('key', models.CharField(max_length=32, unique=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitation_senders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]