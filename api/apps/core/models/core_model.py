from django.db import models
from django.utils.translation import ugettext_lazy as _


class CoreModel(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(_('updated'), auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(_('is active'), default=True)
