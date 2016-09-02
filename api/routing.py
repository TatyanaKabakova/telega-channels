from channels import route, route_class

channel_routing = [
    # route('http.request', 'account.consumers.http_request_consumer'),
    route('send-invite', 'account.consumers.send_invite'),

    route_class('apps.chat.consumers.ChatConsumer', path=r"^/chat/"),
]
