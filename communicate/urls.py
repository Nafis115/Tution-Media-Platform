# urls.py

from django.urls import path
from .views import ConversationListCreateAPIView, MessageListCreateAPIView

urlpatterns = [
    path('conversations/', ConversationListCreateAPIView.as_view(), name='conversation-list-create'),
    path('conversations/<int:conversation_id>/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
]
