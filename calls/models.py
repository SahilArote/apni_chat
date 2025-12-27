from django.db import models
from chat.models import Conversation
from accounts.models import User
# Create your models here.

class Call(models.Model):
    CALL_TYPE = (
        ('audio', 'Audio'),
        ('video', 'Video'),
    )

    STATUS = (
        ('initiated', 'Initiated'),
        ('ringing', 'Ringing'),
        ('ongoing', 'Ongoing'),
        ('ended', 'Ended'),
        ('missed', 'Missed'),
    )

    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='calls'
    )
    caller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='started_calls'
    )

    call_type = models.CharField(max_length=10, choices=CALL_TYPE)
    status = models.CharField(max_length=10, choices=STATUS)

    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)



class CallParticipant(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(null=True, blank=True)
    left_at = models.DateTimeField(null=True, blank=True)

