# routing.py
from channels.routing import route

channel_routing = [
    route('websocket.receive', 'second.consumers.ws_echo'),
]
