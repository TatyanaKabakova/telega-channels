# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class CustomUserManager(UserManager):
    def active(self):
        return self.filter(is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model for User profile.
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username = models.CharField(_('username'), max_length=254, unique=True,
                                error_messages={'unique': _('A user with that username already exists.')})
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=254, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=254, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(_('staff status'), default=False)
    reset_code = models.CharField(_('reset code'), blank=True, null=True, max_length=32, unique=True)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        """
        REQUIRED_FIELDS cannot contain the USERNAME_FIELD in custom User Model. since USERNAME_FIELD = 'email',
        I had to include the 'username' in the REQUIRED_FIELD as otherwise the migration fails for a different reason.
        actual username is unused in our api, so the cleanest way to keep username model field filled and unique is to
        put email value
        """
        self.username = self.email
        super(User, self).save(*args, **kwargs)

    def get_short_name(self) -> str:
        return self.email
