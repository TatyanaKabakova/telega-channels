from django.db import models
from .user import User


class Invitation(models.Model):

    email = models.EmailField()
    sent = models.DateTimeField(null=True)
    sender = models.ForeignKey(User, related_name='invitation_senders')
    key = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{} invited {}".format(self.sender, self.email)
