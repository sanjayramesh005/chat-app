from django.conf.urls import url
from second.views import (
    AddMessageView,
    GetAllMessages,
)

urlpatterns = [
    url(r'^sendmsg', AddMessageView.as_view(), name='add_message_url'),
    url(r'^get_all_msgs', GetAllMessages.as_view(), name='all_messages_url'),
]
