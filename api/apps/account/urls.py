from django.conf.urls import url

from .views import (UserDetailAPIView, UserEmailAPIView)


urlpatterns = [
    url(r'^user/$', UserDetailAPIView.as_view(), name='user_detail'),
    url(r'^email/$', UserEmailAPIView.as_view(), name='user_send_email'),

]
