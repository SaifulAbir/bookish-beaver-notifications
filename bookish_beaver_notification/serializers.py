from rest_framework import serializers


class NotificationSerializer(serializers.Serializer):
    notification = serializers.JSONField()