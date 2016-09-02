from channels import route, route_class

channel_routing = [
    # route('http.request', 'account.consumers.http_request_consumer'),
    route('send-invite', 'account.consumers.send_invite'),
    # route('websocket.connect', 'chat.consumers.ws_connect'),
    # route('websocket.receive', 'chat.consumers.ws_message'),
    # route('websocket.disconnect', 'chat.consumers.ws_disconnect'),

    route_class('apps.chat.consumers.MyConsumer', path=r"^/chat/"),
]
