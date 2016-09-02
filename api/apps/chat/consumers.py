import json
from channels.channel import Group
from channels.generic import BaseConsumer

# def ws_connect(message):
#     Group('chat').add(message.reply_channel)
#
# def ws_message(message):
#     Group('chat').send({'text': json.dumps({'message': message.content['text'],
#                                             'sender': message.reply_channel.name})})
#
# def ws_disconnect(message):
#     Group('chat').discard(message.reply_channel)


class MyConsumer(BaseConsumer):

    method_mapping = {
        "websocket.connect": "ws_connect",
        "websocket.receive": "ws_message",
        "websocket.disconnect": "ws_disconnect",
    }

    def ws_connect(self, message, **kwargs):
        Group('chat').add(message.reply_channel)

    def ws_message(self, message, **kwargs):
        Group('chat').send({'text': json.dumps({'message': message.content['text'],
                                                'sender': message.reply_channel.name})})

    def ws_disconnect(self, message, **kwargs):
        Group('chat').discard(message.reply_channel)
