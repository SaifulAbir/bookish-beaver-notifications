import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class NotificationConsumer(WebsocketConsumer):

    # Function to connect to the websocket
    def connect(self):
        # print(self.scope["user"])   # Can access logged in user details by using self.scope.user, Can only be used if AuthMiddlewareStack is used in the routing.py
        print(self.scope['url_route']['kwargs']['user_id'])
        self.group_name = 'notifications_' + self.scope['url_route']['kwargs']['user_id']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    # Function to disconnet the Socket
    def disconnect(self, close_code):
        self.close()
        # pass

    # Custom Notify Function which can be called from Views or api to send message to the frontend
    def notify(self, event):
        self.send(text_data=json.dumps(event["text"]))