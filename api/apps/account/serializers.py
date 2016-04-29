from channels import Channel

from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Invitation

User = get_user_model()



class UserDetailSerializer(serializers.ModelSerializer):
    """
    Used to display basic fields of user's profile.
    """
    email = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invitation
        fields = ('email',)

    def create(self, validated_data):
        validated_data['sender'] = User.objects.get(pk=1)
        validated_data['key'] = get_random_string(32).lower()
        instance = super(UserEmailSerializer, self).create(validated_data)
        notification = {
            'id': instance.id,
        }
        Channel('send-invite').send(notification)
        return instance
