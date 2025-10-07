from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.ReadOnlyField(source='target_content_type.model')

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_type', 'target_object_id', 'timestamp', 'read']
