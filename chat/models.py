from django.db import models
from accounts.models import User


class Conversation(models.Model):
    CONVERSATION_TYPE = (
        ('private', 'Private'),
        ('group', 'Group'),
    )

    type = models.CharField(max_length=10, choices=CONVERSATION_TYPE)
    name = models.CharField(max_length=255, blank=True)  # group name
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='created_conversations'
    )

    created_at = models.DateTimeField(auto_now_add=True)


class ConversationParticipant(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_muted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('conversation', 'user')


class Message(models.Model):
    MESSAGE_TYPE = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('file', 'File'),
        ('system', 'System'),
    )

    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages'
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages'
    )

    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE)
    content = models.TextField(blank=True)
    media = models.FileField(upload_to='messages/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, blank=True)

class MessageRead(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('message', 'user')
