from django.contrib.auth import get_user_model

from rest_framework.generics import (RetrieveUpdateAPIView, CreateAPIView)

from .serializers import (UserDetailSerializer, UserEmailSerializer)

from .models import Invitation

User = get_user_model()


class UserDetailAPIView(RetrieveUpdateAPIView):
    """
    View to get user's details and update them. Used on user profile page.
    """
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user


class UserEmailAPIView(CreateAPIView):

    model = Invitation
    serializer_class = UserEmailSerializer
