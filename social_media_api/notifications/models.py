from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acted_notifications')
    verb = models.CharField(max_length=255) 
    
    # Generic foreign key to the target object (post, comment, etc.)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def timestamp(self):
        return self.created_at

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'read']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.actor.username} {self.verb} (to {self.recipient.username})"

    def mark_as_read(self):
        """Mark notification as read and save"""
        if not self.read:
            self.read = True
            self.save()

    def mark_as_unread(self):
        """Mark notification as unread and save"""
        if self.read:
            self.read = False
            self.save()