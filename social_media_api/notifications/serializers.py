from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.SerializerMethodField()
    
    def get_target(self, obj):
        if obj.target:
            return str(obj.target)
        return None
    
    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'read', 'created_at']
        read_only_fields = fields