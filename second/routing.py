# routing.py
from channels.routing import route

channel_routing = [
    route('websocket.connect', 'second.consumers.ws_connect'),
    route('websocket.receive', 'second.consumers.ws_receive',),
    route('websocket.disconnect', 'second.consumers.ws_disconnect',),
]
