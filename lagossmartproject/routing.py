from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from websockets.views import TestConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket' : AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('chart', TestConsumer),
            ])
        )
    )
})