import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.views import APIView
from bookish_beaver_notification.serializers import NotificationSerializer
from rest_framework.response import Response


class NotificationAPIView(APIView):

    def post(self, request):
        notification_serializer = NotificationSerializer(data=request.data)
        if notification_serializer.is_valid():
            data = request.data
            channel_layer = get_channel_layer()

            group_name = "notifications"
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'notify',
                    'text': json.loads(data["notification"])
                }
            )
            return Response(data)