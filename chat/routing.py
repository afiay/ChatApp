# In your routing.py file (make sure this is correctly referenced in your ASGI application setup)
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<senderId>\d+)/(?P<recipientId>\d+)/$',
            ChatConsumer.as_asgi()),
]
